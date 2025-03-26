grammar Gramatica;

gramatica
    : VARIABLE LLAVE_APERTURA MAIN LLAVE_APERTURA instruccion* LLAVE_CIERRE LLAVE_CIERRE EOF
    ;

instruccion
    : declaracion_y_asignacion
    | sentencia_print
    | sentencia_if
    | sentencia_while
    | sentencia_for
    ;

declaracion_y_asignacion
    : (tipo)? VARIABLE ASIGNACION expr FIN_DE_LINEA
    ;

tipo
    : INT
    | FLOAT
    | BOOLEAN
    | STRING
    ;

sentencia_print
    : PRINT PARENTESIS_APERTURA expr PARENTESIS_CIERRE FIN_DE_LINEA
    ;

sentencia_if
    : IF PARENTESIS_APERTURA expr PARENTESIS_CIERRE bloque
      (ELSE IF PARENTESIS_APERTURA expr PARENTESIS_CIERRE bloque)*
      (ELSE bloque)?
    ;

sentencia_while
    : WHILE PARENTESIS_APERTURA expr PARENTESIS_CIERRE bloque
    ;

sentencia_for
    : FOR PARENTESIS_APERTURA declaracion_y_asignacion expr FIN_DE_LINEA for_incremento_y_disminucion PARENTESIS_CIERRE bloque
    ;

for_incremento_y_disminucion
    : VARIABLE (MASMAS | MENOSMENOS)//i++ i--
    | declaracion_y_asignacion //i=i+2
    ;

bloque
    : LLAVE_APERTURA instruccion+ LLAVE_CIERRE
    ;

expr
    : expr (POTENCIA | MULTIPLICACION | DIVISION | MAS | MENOS) expr
    | expr (MAYOR | MENOR | MAYOR_IGUAL_QUE | MENOR_IGUAL_QUE | IGUAL | DIFERENTE) expr
    | PARENTESIS_APERTURA expr PARENTESIS_CIERRE
    | VARIABLE
    | NUMERO
    | CADENA
    | BOOLEANO
    ;

MAIN: 'main()';
IF: 'if';
ELSE: 'else';
WHILE: 'while';
FOR: 'for';
PRINT: 'print';
ASIGNACION: '=';

MAS: '+';
MENOS: '-';
MULTIPLICACION: '*';
DIVISION: '/';
POTENCIA: '^';

IGUAL: '==';
DIFERENTE: '!=';
MENOR: '<';
MAYOR: '>';
MENOR_IGUAL_QUE: '<=';
MAYOR_IGUAL_QUE: '>=';

MASMAS: '++';
MENOSMENOS: '--';

INT: 'int';
FLOAT: 'float';
BOOLEAN: 'boolean';
STRING: 'string';

VARIABLE: [a-zA-Z_][a-zA-Z0-9_]*;
NUMERO: [0-9]+ ('.' [0-9]+)?;
CADENA: '"' (~["\r\n])* '"';
BOOLEANO: 'true' | 'false';

PARENTESIS_APERTURA: '(';
PARENTESIS_CIERRE: ')';
LLAVE_APERTURA: '{';
LLAVE_CIERRE: '}';
FIN_DE_LINEA: ';';

WS: [ \t\r\n]+ -> skip;
COMENTARIO_LINEA: '---' ~[\r\n]* -> skip;
COMENTARIO_MULTILINEA: '---' .*? '---' -> skip;