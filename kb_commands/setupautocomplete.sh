#!/bin/bash

function _kbcomplete()
{
    local cur prev commands variables
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"
    commands="addvar list register ssh vars setEnvironment environment"  # todo read this list 'ls  kb*'

    if [[ ${cur} == ^* ]];
    then
        variables=`cat ~/scripts/kb_commands/variables | cut -d" " -f 2 | cut -d"=" -f1`
        variableList=''
        for variable in $variables
        do
            variableList="$variableList ^$variable"
        done <<< ${variables}

        COMPREPLY=( $(compgen -W "${variableList}" ${cur}) ) # autocomplete variables
    elif [[ ${prev} == ssh ]];
    then
        types=`cat ~/scripts/kb_commands/registrations | cut -d" " -f3`
        COMPREPLY=( $(compgen -W "${types}" ${cur}) )
    else
        COMPREPLY=( $(compgen -W "${commands}" ${cur}) )
    fi
}

complete -F _kbcomplete "kb"
