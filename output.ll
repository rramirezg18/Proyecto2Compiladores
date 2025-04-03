; ModuleID = "main"
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

define i32 @"potencia"(i32 %".1", i32 %".2")
{
entry:
  %"base" = alloca i32
  store i32 %".1", i32* %"base"
  %"exponente" = alloca i32
  store i32 %".2", i32* %"exponente"
  %"base.1" = load i32, i32* %"base"
  %"exponente.1" = load i32, i32* %"exponente"
  %".6" = sitofp i32 %"base.1" to double
  %".7" = sitofp i32 %"exponente.1" to double
  %".8" = call double @"llvm.pow.f64"(double %".6", double %".7")
  %".9" = fptosi double %".8" to i32
  ret i32 %".9"
}

define i32 @"sumar"(i32 %".1", i32 %".2")
{
entry:
  %"a" = alloca i32
  store i32 %".1", i32* %"a"
  %"b" = alloca i32
  store i32 %".2", i32* %"b"
  %"a.1" = load i32, i32* %"a"
  %"b.1" = load i32, i32* %"b"
  %".6" = add i32 %"a.1", %"b.1"
  ret i32 %".6"
}

define i32 @"sumaHasta"(i32 %".1")
{
entry:
  %"n" = alloca i32
  store i32 %".1", i32* %"n"
  %"suma" = alloca i32
  store i32 0, i32* %"suma"
  %"contador" = alloca i32
  store i32 1, i32* %"contador"
  br label %"while.cond"
while.cond:
  %"contador.1" = load i32, i32* %"contador"
  %"n.1" = load i32, i32* %"n"
  %".7" = icmp slt i32 %"contador.1", %"n.1"
  br i1 %".7", label %"while.body", label %"while.end"
while.body:
  %"suma.1" = load i32, i32* %"suma"
  %"contador.2" = load i32, i32* %"contador"
  %".9" = add i32 %"suma.1", %"contador.2"
  store i32 %".9", i32* %"suma"
  %"contador.3" = load i32, i32* %"contador"
  %".11" = add i32 %"contador.3", 1
  store i32 %".11", i32* %"contador"
  br label %"while.cond"
while.end:
  %"suma.2" = load i32, i32* %"suma"
  ret i32 %"suma.2"
}

define i32 @"contarHasta"(i32 %".1")
{
entry:
  %"n" = alloca i32
  store i32 %".1", i32* %"n"
  %"i" = alloca i32
  store i32 0, i32* %"i"
  store i32 1, i32* %"i"
  br label %"for.cond"
for.cond:
  %"i.1" = load i32, i32* %"i"
  %"n.1" = load i32, i32* %"n"
  %".7" = icmp sle i32 %"i.1", %"n.1"
  br i1 %".7", label %"for.body", label %"for.exit"
for.body:
  %"i.2" = load i32, i32* %"i"
  %".9" = bitcast [4 x i8]* @"fmt_int" to i8*
  %".10" = call i32 (i8*, ...) @"printf"(i8* %".9", i32 %"i.2")
  br label %"for.inc"
for.inc:
  %"i.3" = load i32, i32* %"i"
  %"i.4" = load i32, i32* %"i"
  %".12" = add i32 %"i.4", 1
  store i32 %".12", i32* %"i"
  br label %"for.cond"
for.exit:
  ret i32 0
}

define i32 @"main"()
{
entry:
  %"x" = alloca i32
  store i32 10, i32* %"x"
  %"y" = alloca double
  store double 0x4039000000000000, double* %"y"
  %"x.1" = load i32, i32* %"x"
  %".4" = bitcast [4 x i8]* @"fmt_int" to i8*
  %".5" = call i32 (i8*, ...) @"printf"(i8* %".4", i32 %"x.1")
  %"y.1" = load double, double* %"y"
  %".6" = bitcast [4 x i8]* @"fmt_float" to i8*
  %".7" = call i32 (i8*, ...) @"printf"(i8* %".6", double %"y.1")
  %"x.2" = load i32, i32* %"x"
  %".8" = icmp sgt i32 %"x.2", 15
  br i1 %".8", label %"then", label %"else"
then:
  %".10" = bitcast [7 x i8]* @"str.3994404365163265527" to i8*
  %".11" = bitcast [4 x i8]* @"fmt_string" to i8*
  %".12" = call i32 (i8*, ...) @"printf"(i8* %".11", i8* %".10")
  br label %"ifcont"
else:
  %".14" = bitcast [11 x i8]* @"str.-7614002029290330855" to i8*
  %".15" = bitcast [4 x i8]* @"fmt_string" to i8*
  %".16" = call i32 (i8*, ...) @"printf"(i8* %".15", i8* %".14")
  br label %"ifcont"
ifcont:
  br label %"while.cond"
while.cond:
  %"x.3" = load i32, i32* %"x"
  %".19" = icmp sgt i32 %"x.3", 0
  br i1 %".19", label %"while.body", label %"while.end"
while.body:
  %"x.4" = load i32, i32* %"x"
  %".21" = bitcast [4 x i8]* @"fmt_int" to i8*
  %".22" = call i32 (i8*, ...) @"printf"(i8* %".21", i32 %"x.4")
  %"x.5" = load i32, i32* %"x"
  %".23" = sub i32 %"x.5", 1
  store i32 %".23", i32* %"x"
  br label %"while.cond"
while.end:
  %"i" = alloca i32
  store i32 0, i32* %"i"
  br label %"for.cond"
for.cond:
  %"i.1" = load i32, i32* %"i"
  %".28" = icmp slt i32 %"i.1", 3
  br i1 %".28", label %"for.body", label %"for.exit"
for.body:
  %"i.2" = load i32, i32* %"i"
  %".30" = bitcast [4 x i8]* @"fmt_int" to i8*
  %".31" = call i32 (i8*, ...) @"printf"(i8* %".30", i32 %"i.2")
  br label %"for.inc"
for.inc:
  %"i.3" = load i32, i32* %"i"
  %"i.4" = load i32, i32* %"i"
  %".33" = add i32 %"i.4", 1
  store i32 %".33", i32* %"i"
  br label %"for.cond"
for.exit:
  %".36" = call i32 @"contarHasta"(i32 5)
  %".37" = call i32 @"potencia"(i32 2, i32 3)
  %".38" = bitcast [4 x i8]* @"fmt_int" to i8*
  %".39" = call i32 (i8*, ...) @"printf"(i8* %".38", i32 %".37")
  %".40" = call i32 @"sumar"(i32 5, i32 7)
  %".41" = bitcast [4 x i8]* @"fmt_int" to i8*
  %".42" = call i32 (i8*, ...) @"printf"(i8* %".41", i32 %".40")
  %"resultado" = alloca i32
  %".43" = call i32 @"sumaHasta"(i32 5)
  store i32 %".43", i32* %"resultado"
  %"resultado.1" = load i32, i32* %"resultado"
  %".45" = bitcast [4 x i8]* @"fmt_int" to i8*
  %".46" = call i32 (i8*, ...) @"printf"(i8* %".45", i32 %"resultado.1")
  %".47" = mul i32 2, 5
  %".48" = bitcast [4 x i8]* @"fmt_int" to i8*
  %".49" = call i32 (i8*, ...) @"printf"(i8* %".48", i32 %".47")
  %"x.6" = load i32, i32* %"x"
  %".50" = mul i32 %"x.6", 4
  %".51" = add i32 2, %".50"
  %".52" = bitcast [4 x i8]* @"fmt_int" to i8*
  %".53" = call i32 (i8*, ...) @"printf"(i8* %".52", i32 %".51")
  %".54" = add i32 2, 3
  %".55" = mul i32 %".54", 4
  %".56" = bitcast [4 x i8]* @"fmt_int" to i8*
  %".57" = call i32 (i8*, ...) @"printf"(i8* %".56", i32 %".55")
  %".58" = sitofp i32 10 to double
  %".59" = sitofp i32 2 to double
  %".60" = fdiv double %".58", %".59"
  %".61" = bitcast [4 x i8]* @"fmt_float" to i8*
  %".62" = call i32 (i8*, ...) @"printf"(i8* %".61", double %".60")
  %".63" = sitofp i32 2 to double
  %".64" = sitofp i32 3 to double
  %".65" = call double @"llvm.pow.f64"(double %".63", double %".64")
  %".66" = bitcast [4 x i8]* @"fmt_float" to i8*
  %".67" = call i32 (i8*, ...) @"printf"(i8* %".66", double %".65")
  %".68" = sitofp i32 3 to double
  %".69" = sitofp i32 2 to double
  %".70" = call double @"llvm.pow.f64"(double %".68", double %".69")
  %".71" = sitofp i32 2 to double
  %".72" = call double @"llvm.pow.f64"(double %".71", double %".70")
  %".73" = bitcast [4 x i8]* @"fmt_float" to i8*
  %".74" = call i32 (i8*, ...) @"printf"(i8* %".73", double %".72")
  %".75" = mul i32 3, 2
  %".76" = add i32 5, %".75"
  %".77" = sitofp i32 4 to double
  %".78" = sitofp i32 2 to double
  %".79" = fdiv double %".77", %".78"
  %".80" = sitofp i32 %".76" to double
  %".81" = fsub double %".80", %".79"
  %".82" = bitcast [4 x i8]* @"fmt_float" to i8*
  %".83" = call i32 (i8*, ...) @"printf"(i8* %".82", double %".81")
  %".84" = add i32 3, 4
  %".85" = sitofp i32 2 to double
  %".86" = sitofp i32 3 to double
  %".87" = call double @"llvm.pow.f64"(double %".85", double %".86")
  %".88" = sitofp i32 %".84" to double
  %".89" = fmul double %".88", %".87"
  %".90" = sitofp i32 10 to double
  %".91" = sitofp i32 2 to double
  %".92" = fdiv double %".90", %".91"
  %".93" = fsub double %".89", %".92"
  %".94" = bitcast [4 x i8]* @"fmt_float" to i8*
  %".95" = call i32 (i8*, ...) @"printf"(i8* %".94", double %".93")
  %".96" = sitofp i32 5 to double
  %".97" = sitofp i32 2 to double
  %".98" = fdiv double %".96", %".97"
  %".99" = bitcast [4 x i8]* @"fmt_float" to i8*
  %".100" = call i32 (i8*, ...) @"printf"(i8* %".99", double %".98")
  %".101" = sub i32 0, 2
  %".102" = mul i32 4, %".101"
  %".103" = add i32 2, %".102"
  %".104" = bitcast [4 x i8]* @"fmt_int" to i8*
  %".105" = call i32 (i8*, ...) @"printf"(i8* %".104", i32 %".103")
  ret i32 0
}

@"fmt_int" = internal constant [4 x i8] c"%d\0a\00"
@"fmt_float" = internal constant [4 x i8] c"%f\0a\00"
@"str.3994404365163265527" = internal constant [7 x i8] c"x > 15\00"
@"fmt_string" = internal constant [4 x i8] c"%s\0a\00"
@"str.-7614002029290330855" = internal constant [11 x i8] c"x es <= 15\00"
declare double @"llvm.pow.f64"(double %".1", double %".2")
