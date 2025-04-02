; ModuleID = "main"
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

define double @"celsiusAFahrenheit"(double %".1")
{
entry:
  %"c" = alloca double
  store double %".1", double* %"c"
  %"c.1" = load double, double* %"c"
  %".4" = sitofp i32 9 to double
  %".5" = fmul double %"c.1", %".4"
  %".6" = sitofp i32 5 to double
  %".7" = fdiv double %".5", %".6"
  %".8" = sitofp i32 32 to double
  %".9" = fadd double %".7", %".8"
  %"f" = alloca double
  store double %".9", double* %"f"
  %"f.1" = load double, double* %"f"
  ret double %"f.1"
}

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
  %".10" = bitcast [20 x i8]* @"str.6237217392754884652" to i8*
  %".11" = bitcast [4 x i8]* @"fmt_string" to i8*
  %".12" = call i32 (i8*, ...) @"printf"(i8* %".11", i8* %".10")
  br label %"ifcont"
else:
  %".14" = bitcast [24 x i8]* @"str.4949494648061565420" to i8*
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
  %".35" = sitofp i32 0 to double
  %".36" = call double @"celsiusAFahrenheit"(double %".35")
  %"result" = alloca double
  store double %".36", double* %"result"
  %"result.1" = load double, double* %"result"
  %".38" = bitcast [4 x i8]* @"fmt_float" to i8*
  %".39" = call i32 (i8*, ...) @"printf"(i8* %".38", double %"result.1")
  %".40" = call i32 @"potencia"(i32 2, i32 3)
  %".41" = bitcast [4 x i8]* @"fmt_int" to i8*
  %".42" = call i32 (i8*, ...) @"printf"(i8* %".41", i32 %".40")
  %".43" = call i32 @"sumar"(i32 5, i32 7)
  %".44" = bitcast [4 x i8]* @"fmt_int" to i8*
  %".45" = call i32 (i8*, ...) @"printf"(i8* %".44", i32 %".43")
  %".46" = call i32 @"sumaHasta"(i32 5)
  %"resultado" = alloca i32
  store i32 %".46", i32* %"resultado"
  %"resultado.1" = load i32, i32* %"resultado"
  %".48" = bitcast [4 x i8]* @"fmt_int" to i8*
  %".49" = call i32 (i8*, ...) @"printf"(i8* %".48", i32 %"resultado.1")
  %".50" = mul i32 2, 5
  %".51" = bitcast [4 x i8]* @"fmt_int" to i8*
  %".52" = call i32 (i8*, ...) @"printf"(i8* %".51", i32 %".50")
  %"x.6" = load i32, i32* %"x"
  %".53" = mul i32 %"x.6", 4
  %".54" = add i32 2, %".53"
  %".55" = bitcast [4 x i8]* @"fmt_int" to i8*
  %".56" = call i32 (i8*, ...) @"printf"(i8* %".55", i32 %".54")
  %".57" = add i32 2, 3
  %".58" = mul i32 %".57", 4
  %".59" = bitcast [4 x i8]* @"fmt_int" to i8*
  %".60" = call i32 (i8*, ...) @"printf"(i8* %".59", i32 %".58")
  %".61" = sdiv i32 10, 2
  %".62" = bitcast [4 x i8]* @"fmt_int" to i8*
  %".63" = call i32 (i8*, ...) @"printf"(i8* %".62", i32 %".61")
  %".64" = sitofp i32 2 to double
  %".65" = sitofp i32 3 to double
  %".66" = call double @"llvm.pow.f64"(double %".64", double %".65")
  %".67" = bitcast [4 x i8]* @"fmt_float" to i8*
  %".68" = call i32 (i8*, ...) @"printf"(i8* %".67", double %".66")
  %".69" = sitofp i32 3 to double
  %".70" = sitofp i32 2 to double
  %".71" = call double @"llvm.pow.f64"(double %".69", double %".70")
  %".72" = sitofp i32 2 to double
  %".73" = call double @"llvm.pow.f64"(double %".72", double %".71")
  %".74" = bitcast [4 x i8]* @"fmt_float" to i8*
  %".75" = call i32 (i8*, ...) @"printf"(i8* %".74", double %".73")
  %".76" = mul i32 3, 2
  %".77" = add i32 5, %".76"
  %".78" = sdiv i32 4, 2
  %".79" = sub i32 %".77", %".78"
  %".80" = bitcast [4 x i8]* @"fmt_int" to i8*
  %".81" = call i32 (i8*, ...) @"printf"(i8* %".80", i32 %".79")
  %".82" = add i32 3, 4
  %".83" = sitofp i32 2 to double
  %".84" = sitofp i32 3 to double
  %".85" = call double @"llvm.pow.f64"(double %".83", double %".84")
  %".86" = sitofp i32 %".82" to double
  %".87" = fmul double %".86", %".85"
  %".88" = sdiv i32 10, 2
  %".89" = sitofp i32 %".88" to double
  %".90" = fsub double %".87", %".89"
  %".91" = bitcast [4 x i8]* @"fmt_float" to i8*
  %".92" = call i32 (i8*, ...) @"printf"(i8* %".91", double %".90")
  %".93" = sdiv i32 5, 2
  %".94" = bitcast [4 x i8]* @"fmt_int" to i8*
  %".95" = call i32 (i8*, ...) @"printf"(i8* %".94", i32 %".93")
  %".96" = sub i32 0, 2
  %".97" = mul i32 4, %".96"
  %".98" = add i32 2, %".97"
  %".99" = bitcast [4 x i8]* @"fmt_int" to i8*
  %".100" = call i32 (i8*, ...) @"printf"(i8* %".99", i32 %".98")
  ret i32 0
}

@"fmt_int" = internal constant [4 x i8] c"%d\0a\00"
@"fmt_float" = internal constant [4 x i8] c"%f\0a\00"
@"str.6237217392754884652" = internal constant [20 x i8] c"x is greater than 5\00"
@"fmt_string" = internal constant [4 x i8] c"%s\0a\00"
@"str.4949494648061565420" = internal constant [24 x i8] c"x is less or equal to 5\00"
declare double @"llvm.pow.f64"(double %".1", double %".2")
