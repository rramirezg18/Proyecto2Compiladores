; ModuleID = "main"
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  %"x" = alloca i32
  store i32 1, i32* %"x"
  %"y" = alloca i32
  store i32 1, i32* %"y"
  %"x.1" = load i32, i32* %"x"
  %"y.1" = load i32, i32* %"y"
  %".4" = add i32 %"x.1", %"y.1"
  %"z" = alloca i32
  store i32 %".4", i32* %"z"
  %"z.1" = load i32, i32* %"z"
  %".6" = bitcast [4 x i8]* @"fmt_int" to i8*
  %".7" = call i32 (i8*, ...) @"printf"(i8* %".6", i32 %"z.1")
  %"a" = alloca i32
  store i32 2, i32* %"a"
  %"b" = alloca i32
  store i32 3, i32* %"b"
  %"a.1" = load i32, i32* %"a"
  %"b.1" = load i32, i32* %"b"
  %".10" = add i32 %"a.1", %"b.1"
  %"r" = alloca i32
  store i32 %".10", i32* %"r"
  %"r.1" = load i32, i32* %"r"
  %".12" = bitcast [4 x i8]* @"fmt_int" to i8*
  %".13" = call i32 (i8*, ...) @"printf"(i8* %".12", i32 %"r.1")
  %"f" = alloca double
  store double 0x4002666666666666, double* %"f"
  %"g" = alloca double
  store double 0x400199999999999a, double* %"g"
  %"f.1" = load double, double* %"f"
  %"g.1" = load double, double* %"g"
  %".16" = fadd double %"f.1", %"g.1"
  %"res" = alloca double
  store double %".16", double* %"res"
  %"res.1" = load double, double* %"res"
  %".18" = bitcast [4 x i8]* @"fmt_float" to i8*
  %".19" = call i32 (i8*, ...) @"printf"(i8* %".18", double %"res.1")
  %".20" = bitcast [5 x i8]* @"str.4523550976541149131" to i8*
  %"k" = alloca i8*
  store i8* %".20", i8** %"k"
  %"k.1" = load i8*, i8** %"k"
  %".22" = bitcast [4 x i8]* @"fmt_string" to i8*
  %".23" = call i32 (i8*, ...) @"printf"(i8* %".22", i8* %"k.1")
  %".24" = add i32 2, 3
  %"NuM1" = alloca i32
  store i32 %".24", i32* %"NuM1"
  %"nuM2" = alloca i32
  store i32 5, i32* %"nuM2"
  %"NuM1.1" = load i32, i32* %"NuM1"
  %"nuM2.1" = load i32, i32* %"nuM2"
  %".27" = add i32 %"NuM1.1", %"nuM2.1"
  %"resultado" = alloca i32
  store i32 %".27", i32* %"resultado"
  %"resultado.1" = load i32, i32* %"resultado"
  %".29" = bitcast [4 x i8]* @"fmt_int" to i8*
  %".30" = call i32 (i8*, ...) @"printf"(i8* %".29", i32 %"resultado.1")
  ret i32 0
}

@"fmt_int" = internal constant [4 x i8] c"%d\0a\00"
@"fmt_float" = internal constant [4 x i8] c"%f\0a\00"
@"str.4523550976541149131" = internal constant [5 x i8] c"hola\00"
@"fmt_string" = internal constant [4 x i8] c"%s\0a\00"