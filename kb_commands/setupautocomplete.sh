#!/bin/bash

function _kbcomplete()
{
    home=~/dev/kb/kb_commands
    local cur prev commands variables
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"

    if [[ ${cur} == ^* ]];
    then
        variables=`cat $home/variables | cut -d" " -f 2 | cut -d"=" -f1`
        variableList=''
        for variable in $variables
        do
            variableList="$variableList ^$variable"
        done <<< ${variables}

        COMPREPLY=( $(compgen -W "${variableList}" ${cur}) ) # autocomplete variables
    elif [[ ${prev} == list ]];
    then
        types=`cat $home/registrations | cut -d" " -f4`
        COMPREPLY=( $(compgen -W "${types}" ${cur}) )
    elif [[ ${prev} == ssh || ${prev} == scp ]];
    then
        types=`cat $home/registrations | cut -d" " -f4`
        COMPREPLY=( $(compgen -W "${types}" ${cur}) )
    elif [[ ${prev} == machines || ${prev} == services || ${prev} == serviceProperties ]];
    then
        environments=`cat $home/registrations | cut -d" " -f2`
        COMPREPLY=( $(compgen -W "${environments}" ${cur}) )
    elif [[ ${COMP_CWORD} -gt 3 &&  ${COMP_WORDS[1]} == scp ]];
    then
        COMPREPLY=($(compgen -fd ${cur} ))
    else
        commands=`ls $home | grep kb_ | awk '{print substr($1, 4);}'`
        COMPREPLY=( $(compgen -W "${commands}" ${cur}) )
    fi
}

complete -F _kbcomplete "kb"
