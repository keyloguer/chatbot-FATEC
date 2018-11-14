## Story 1
* greet
    - utter_greet
>check_servico

## Story 1
* greet
    - utter_greet
>check_goodbye

## Story 1
* greet
    - utter_greet
>check_greet

## Story 1
>check_greet
* greet
    - utter_greet
>check_servico

## Story 1
>check_greet_cursos
* greet
    - utter_greet_cursos
>check_goodbye

## Story 1
>check_greet_cursos
* greet
    - utter_greet_cursos
>check_cursos

## Story 1
>check_greet_cursos
* greet
    - utter_greet_cursos
>check_goodbye

# Story 2
>check_servico
* servico{"setor": "atendimento"}
    - slot {"setor": "atendimento"}
    - action_check_servico
>check_greet

# Story 2
>check_servico
* servico{"setor": "atendimento"}
    - slot {"setor": "atendimento"}
    - action_check_servico
>check_servico

# Story 2
>check_servico
* servico{"setor": "atendimento"}
    - slot {"setor": "atendimento"}
    - action_check_servico
>check_ofensa

# Story 2
>check_servico
* servico{"setor": "onde fica"}
    - slot {"setor": "onde fica"}
    - action_check_servico
>check_greet

# Story 2
>check_servico
* servico{"setor": "onde fica"}
    - slot {"setor": "onde fica"}
    - action_check_servico
>check_servico

# Story 2
>check_servico
* servico{"setor": "onde fica"}
    - slot {"setor": "onde fica"}
    - action_check_servico
>check_ofensa

# Story 2
>check_servico
* servico{"setor": "cursos"}
    - slot {"setor": "cursos"}
    - action_check_servico
>check_greet

# Story 2
>check_servico
* servico{"setor": "cursos"}
    - slot {"setor": "cursos"}
    - action_check_servico
>check_cursos

# Story 2
>check_servico
* servico{"setor": "cursos"}
    - slot {"setor": "cursos"}
    - action_check_servico
>check_ofensa_curso

# Story 2
>check_servico
* servico{"setor": "coordenação"}
    - slot {"setor": "coordenação"}
    - action_check_servico
>check_greet

# Story 2
>check_servico
* servico{"setor": "coordenação"}
    - slot {"setor": "coordenação"}
    - action_check_servico
>check_servico

# Story 2
>check_servico
* servico{"setor": "coordenação"}
    - slot {"setor": "coordenação"}
    - action_check_servico
>check_ofensa

# Story 2
>check_cursos
* cursos{"area": "gestão portuária"}
    - slot {"area": "gestão portuária"}
    - action_check_cursos
>check_cursos

# Story 2
>check_cursos
* cursos{"area": "gestão portuária"}
    - slot {"area": "gestão portuária"}
    - action_check_cursos
>check_servico

# Story 2
>check_cursos
* cursos{"area": "gestão portuária"}
    - slot {"area": "gestão portuária"}
    - action_check_cursos
>check_greet_cursos

# Story 2
>check_cursos
* cursos{"area": "gestão portuária"}
    - slot {"area": "gestão portuária"}
    - action_check_cursos
>check_ofensa_curso

# Story 2
>check_cursos
* cursos{"area": "gestão portuária"}
    - slot {"area": "gestão portuária"}
    - action_check_cursos
>check_goodbye

# Story 2
>check_cursos
* cursos{"area": "gestão empresarial"}
    - slot {"area": "gestão empresarial"}
    - action_check_cursos
>check_cursos

# Story 2
>check_cursos
* cursos{"area": "gestão empresarial"}
    - slot {"area": "gestão empresarial"}
    - action_check_cursos
>check_servico

# Story 2
>check_cursos
* cursos{"area": "gestão empresarial"}
    - slot {"area": "gestão empresarial"}
    - action_check_cursos
>check_greet_cursos

# Story 2
>check_cursos
* cursos{"area": "gestão empresarial"}
    - slot {"area": "gestão empresarial"}
    - action_check_cursos
>check_ofensa_curso

# Story 2
>check_cursos
* cursos{"area": "gestão empresarial"}
    - slot {"area": "gestão empresarial"}
    - action_check_cursos
>check_goodbye

# Story 2
>check_cursos
* cursos{"area": "análise e desenvolvimento de sistemas"}
    - slot {"area": "análise e desenvolvimento de sistemas"}
    - action_check_cursos
>check_cursos

# Story 2
>check_cursos
* cursos{"area": "análise e desenvolvimento de sistemas"}
    - slot {"area": "análise e desenvolvimento de sistemas"}
    - action_check_cursos
>check_servico

# Story 2
>check_cursos
* cursos{"area": "análise e desenvolvimento de sistemas"}
    - slot {"area": "análise e desenvolvimento de sistemas"}
    - action_check_cursos
>check_greet_cursos

# Story 2
>check_cursos
* cursos{"area": "análise e desenvolvimento de sistemas"}
    - slot {"area": "análise e desenvolvimento de sistemas"}
    - action_check_cursos
>check_ofensa_curso

# Story 2
>check_cursos
* cursos{"area": "análise e desenvolvimento de sistemas"}
    - slot {"area": "análise e desenvolvimento de sistemas"}
    - action_check_cursos
>check_goodbye

# Story 2
>check_cursos
* cursos{"area": "logística"}
    - slot {"area": "logística"}
    - action_check_cursos
>check_cursos

# Story 2
>check_cursos
* cursos{"area": "logística"}
    - slot {"area": "logística"}
    - action_check_cursos
>check_servico

# Story 2
>check_cursos
* cursos{"area": "logística"}
    - slot {"area": "logística"}
    - action_check_cursos
>check_greet_cursos

# Story 2
>check_cursos
* cursos{"area": "logística"}
    - slot {"area": "logística"}
    - action_check_cursos
>check_ofensa_curso

# Story 2
>check_cursos
* cursos{"area": "logística"}
    - slot {"area": "logística"}
    - action_check_cursos
>check_goodbye

# Story 2
>check_cursos
* cursos{"area": "sistemas para internet"}
    - slot {"area": "sistemas para internet"}
    - action_check_cursos
>check_cursos

# Story 2
>check_cursos
* cursos{"area": "sistemas para internet"}
    - slot {"area": "sistemas para internet"}
    - action_check_cursos
>check_servico

# Story 2
>check_cursos
* cursos{"area": "sistemas para internet"}
    - slot {"area": "sistemas para internet"}
    - action_check_cursos
>check_greet_cursos

# Story 2
>check_cursos
* cursos{"area": "sistemas para internet"}
    - slot {"area": "sistemas para internet"}
    - action_check_cursos
>check_ofensa_curso

# Story 2
>check_cursos
* cursos{"area": "sistemas para internet"}
    - slot {"area": "sistemas para internet"}
    - action_check_cursos
>check_goodbye

# Story 3
>check_ofensa
* ofensa
    - utter_ofensa
>check_ofensa

# Story 3
>check_ofensa
* ofensa
    - utter_ofensa
>check_servico

# Story 3
>check_ofensa
* ofensa
    - utter_ofensa
>check_goodbye

# Story 3
>check_ofensa_curso
* ofensa
    - utter_ofensa
>check_ofensa_curso

# Story 3
>check_ofensa_curso
* ofensa
    - utter_ofensa
>check_curso

# Story 3
>check_ofensa_curso
* ofensa
    - utter_ofensa
>check_goodbye

## Story 8
>check_goodbye
* goodbye
    - utter_goodbye