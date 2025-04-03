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
  %"i_inc" = add i32 %"i.3", 1
  store i32 %"i_inc", i32* %"i"
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
  %".8" = icmp sgt i32 %"x.2", 5
  br i1 %".8", label %"then", label %"else"
then:
  %".10" = bitcast [17 x i8]* @"str.5694196220069573191" to i8*
  %".11" = bitcast [4 x i8]* @"fmt_string" to i8*
  %".12" = call i32 (i8*, ...) @"printf"(i8* %".11", i8* %".10")
  br label %"ifcont"
else:
  %".14" = bitcast [25 x i8]* @"str.-557817373700032577" to i8*
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
  %"i_inc" = add i32 %"i.3", 1
  store i32 %"i_inc", i32* %"i"
  br label %"for.cond"
for.exit:
  %".35" = call i32 @"contarHasta"(i32 5)
  %".36" = call i32 @"potencia"(i32 2, i32 3)
  %".37" = bitcast [4 x i8]* @"fmt_int" to i8*
  %".38" = call i32 (i8*, ...) @"printf"(i8* %".37", i32 %".36")
  %".39" = call i32 @"sumar"(i32 5, i32 7)
  %".40" = bitcast [4 x i8]* @"fmt_int" to i8*
  %".41" = call i32 (i8*, ...) @"printf"(i8* %".40", i32 %".39")
  %".42" = call i32 @"sumaHasta"(i32 5)
  %"resultado" = alloca i32
  store i32 %".42", i32* %"resultado"
  %"resultado.1" = load i32, i32* %"resultado"
  %".44" = bitcast [4 x i8]* @"fmt_int" to i8*
  %".45" = call i32 (i8*, ...) @"printf"(i8* %".44", i32 %"resultado.1")
  %".46" = mul i32 2, 5
  %".47" = bitcast [4 x i8]* @"fmt_int" to i8*
  %".48" = call i32 (i8*, ...) @"printf"(i8* %".47", i32 %".46")
  %"x.6" = load i32, i32* %"x"
  %".49" = mul i32 %"x.6", 4
  %".50" = add i32 2, %".49"
  %".51" = bitcast [4 x i8]* @"fmt_int" to i8*
  %".52" = call i32 (i8*, ...) @"printf"(i8* %".51", i32 %".50")
  %".53" = add i32 2, 3
  %".54" = mul i32 %".53", 4
  %".55" = bitcast [4 x i8]* @"fmt_int" to i8*
  %".56" = call i32 (i8*, ...) @"printf"(i8* %".55", i32 %".54")
  %".57" = sdiv i32 10, 2
  %".58" = bitcast [4 x i8]* @"fmt_int" to i8*
  %".59" = call i32 (i8*, ...) @"printf"(i8* %".58", i32 %".57")
  %".60" = sitofp i32 2 to double
  %".61" = sitofp i32 3 to double
  %".62" = call double @"llvm.pow.f64"(double %".60", double %".61")
  %".63" = bitcast [4 x i8]* @"fmt_float" to i8*
  %".64" = call i32 (i8*, ...) @"printf"(i8* %".63", double %".62")
  %".65" = sitofp i32 3 to double
  %".66" = sitofp i32 2 to double
  %".67" = call double @"llvm.pow.f64"(double %".65", double %".66")
  %".68" = sitofp i32 2 to double
  %".69" = call double @"llvm.pow.f64"(double %".68", double %".67")
  %".70" = bitcast [4 x i8]* @"fmt_float" to i8*
  %".71" = call i32 (i8*, ...) @"printf"(i8* %".70", double %".69")
  %".72" = mul i32 3, 2
  %".73" = add i32 5, %".72"
  %".74" = sdiv i32 4, 2
  %".75" = sub i32 %".73", %".74"
  %".76" = bitcast [4 x i8]* @"fmt_int" to i8*
  %".77" = call i32 (i8*, ...) @"printf"(i8* %".76", i32 %".75")
  %".78" = add i32 3, 4
  %".79" = sitofp i32 2 to double
  %".80" = sitofp i32 3 to double
  %".81" = call double @"llvm.pow.f64"(double %".79", double %".80")
  %".82" = sitofp i32 %".78" to double
  %".83" = fmul double %".82", %".81"
  %".84" = sdiv i32 10, 2
  %".85" = sitofp i32 %".84" to double
  %".86" = fsub double %".83", %".85"
  %".87" = bitcast [4 x i8]* @"fmt_float" to i8*
  %".88" = call i32 (i8*, ...) @"printf"(i8* %".87", double %".86")
  %".89" = sdiv i32 5, 2
  %".90" = bitcast [4 x i8]* @"fmt_int" to i8*
  %".91" = call i32 (i8*, ...) @"printf"(i8* %".90", i32 %".89")
  %".92" = sub i32 0, 2
  %".93" = mul i32 4, %".92"
  %".94" = add i32 2, %".93"
  %".95" = bitcast [4 x i8]* @"fmt_int" to i8*
  %".96" = call i32 (i8*, ...) @"printf"(i8* %".95", i32 %".94")
  ret i32 0
}

@"fmt_int" = internal constant [4 x i8] c"%d\0a\00"
@"fmt_float" = internal constant [4 x i8] c"%f\0a\00"
@"str.5694196220069573191" = internal constant [17 x i8] c"x es mayor que 5\00"
@"fmt_string" = internal constant [4 x i8] c"%s\0a\00"
@"str.-557817373700032577" = internal constant [25 x i8] c"x es menor o igual que 5\00"
declare double @"llvm.pow.f64"(double %".1", double %".2")
