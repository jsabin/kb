#!/bin/bash

function _kbcomplete()
{
    home=~/dev/kb/kb_commands
    local cur prev commands variables
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"
    commands="addvar list register ssh vars setEnvironment environment"  # todo read this list 'ls  kb*'

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
    elif [[ ${prev} == ssh ]];
    then
        types=`cat $home/registrations | cut -d" " -f4`
        COMPREPLY=( $(compgen -W "${types}" ${cur}) )
    else
        COMPREPLY=( $(compgen -W "${commands}" ${cur}) )
    fi
}

complete -F _kbcomplete "kb"
