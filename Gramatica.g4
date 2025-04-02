/*
ESTRUCTURA DEL LENGUAGEJE
programx{
    main(){ -->funcion principal
        bloque deinstrucciones
    }
    tipo funcion(parametros o no){ --> demas funciones
        bloque instrucciones
    }
}
*/

grammar Gramatica;

gramatica
    : VARIABLE LLAVE_APERTURA main funcion* LLAVE_CIERRE EOF
    ;

//funcion principal programX{main(){instrucciones} funciones{}}
main
    : MAIN PARENTESIS_APERTURA PARENTESIS_CIERRE LLAVE_APERTURA instruccion* LLAVE_CIERRE
    ;

instruccion
    : declaracion_y_asignacion
    | sentencia_print
    | sentencia_if
    | sentencia_while
    | sentencia_for
    | sentencia_return
    | llamada_funcion
    ;
// int, string, float, boolean variable = expresion;
declaracion_y_asignacion
    : (tipo)? VARIABLE ASIGNACION expr FIN_DE_LINEA
    ;

tipo
    : INT
    | FLOAT
    | BOOLEAN
    | STRING
    ;

//print(expresion);
sentencia_print
    : PRINT PARENTESIS_APERTURA expr PARENTESIS_CIERRE FIN_DE_LINEA
    ;

//if(expresion){bloque de instrucciones}else if(expresion){instrucciones}else{instrucciones}
sentencia_if
    : IF PARENTESIS_APERTURA expr PARENTESIS_CIERRE bloque
      (ELSE IF PARENTESIS_APERTURA expr PARENTESIS_CIERRE bloque)*
      (ELSE bloque)?
    ;

//while(expresion){instrucciones}
sentencia_while
    : WHILE PARENTESIS_APERTURA expr PARENTESIS_CIERRE bloque
    ;

//for(expresion){bloque de instrucciones}
sentencia_for
    : FOR PARENTESIS_APERTURA declaracion_y_asignacion expr FIN_DE_LINEA for_incremento_y_disminucion PARENTESIS_CIERRE bloque
    ;

for_incremento_y_disminucion
    : VARIABLE (MASMAS | MENOSMENOS) // i++ i--
    | declaracion_y_asignacion // i = i + 2
    ;

sentencia_return
    : RETURN expr FIN_DE_LINEA
    ;

//tipo funcion(parametros) {bloque de instrucciones p}
funcion
    : tipo VARIABLE PARENTESIS_APERTURA parametros? PARENTESIS_CIERRE LLAVE_APERTURA instruccion* (sentencia_return)? LLAVE_CIERRE
    ;
//(tipo variable, tipo variable etc.)
parametros
    : tipo VARIABLE (COMA tipo VARIABLE)*
    ;

//arguentos a pasar cuando se llama una funcion
argumentos
    : expr (COMA expr)*
    ;
//nombreFuncion(argumentos);
llamada_funcion
    : VARIABLE PARENTESIS_APERTURA argumentos? PARENTESIS_CIERRE FIN_DE_LINEA?
    ;
{bloque de instrucciones}
bloque
    : LLAVE_APERTURA instruccion+ LLAVE_CIERRE
    ;
//Exppresiones
expr
    : <assoc=right> expr POTENCIA expr       // Mayor precedencia
    | expr (MULTIPLICACION | DIVISION | MOD) expr
    | expr (MAS | MENOS) expr
    | expr (MAYOR | MENOR | MAYOR_IGUAL_QUE | MENOR_IGUAL_QUE | IGUAL | DIFERENTE) expr
    | MENOS expr  // Negación unaria (colocada después para evitar ambigüedad)
    | PARENTESIS_APERTURA expr PARENTESIS_CIERRE  // Agrupación con paréntesis
    | llamada_funcion
    | VARIABLE
    | NUMERO
    | CADENA
    | BOOLEANO
    ;

//instrucciones
MAIN: 'main';
IF: 'if';
ELSE: 'else';
WHILE: 'while';
FOR: 'for';
PRINT: 'print';
RETURN: 'return';
ASIGNACION: '=';

//matematicos
MAS: '+';
MENOS: '-';
MULTIPLICACION: '*';
DIVISION: '/';
POTENCIA: '^';
MOD:'%';
//operadores para validar
IGUAL: '==';
DIFERENTE: '!=';
MENOR: '<';
MAYOR: '>';
MENOR_IGUAL_QUE: '<=';
MAYOR_IGUAL_QUE: '>=';

//para hacer incremento_y_disminucion
MASMAS: '++';
MENOSMENOS: '--';
//tipos de dato
INT: 'int';
FLOAT: 'float';
BOOLEAN: 'boolean';
STRING: 'string';

//valores que pueden tomar las variables y su identificador
VARIABLE: [a-zA-Z_][a-zA-Z0-9_]*;//identificador
NUMERO: [0-9]+ ('.' [0-9]+)?;
CADENA: '"' (~["\r\n])* '"';
BOOLEANO: 'true' | 'false';

//Delimitadores
PARENTESIS_APERTURA: '(';
PARENTESIS_CIERRE: ')';
LLAVE_APERTURA: '{';
LLAVE_CIERRE: '}';
FIN_DE_LINEA: ';';
COMA: ',';
//ignora estos caracteres
WS: [ \t\r\n]+ -> skip;
COMENTARIO_LINEA: '//' ~[\r\n]* -> skip;
COMENTARIO_MULTILINEA: '//' .*? '///' -> skip;
