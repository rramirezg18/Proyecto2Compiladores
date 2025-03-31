; ModuleID = "mi_modulo"
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  %".2" = sitofp i32 10 to double
  %"x" = alloca double
  store double %".2", double* %"x"
  %".4" = sitofp i32 20 to double
  %"y" = alloca double
  store double %".4", double* %"y"
  %"x.1" = load double, double* %"x"
  %"y.1" = load double, double* %"y"
  %".6" = sitofp i32 2 to double
  %".7" = fmul double %"y.1", %".6"
  %".8" = fadd double %"x.1", %".7"
  %"z" = alloca double
  store double %".8", double* %"z"
  %".10" = sitofp i32 0 to double
  %"w" = alloca double
  store double %".10", double* %"w"
  %"z.1" = load double, double* %"z"
  %".12" = sitofp i32 30 to double
  %".13" = fcmp ogt double %"z.1", %".12"
  br i1 %".13", label %"then", label %"else"
then:
  %"z.2" = load double, double* %"z"
  %".15" = sitofp i32 2 to double
  %".16" = fdiv double %"z.2", %".15"
  store double %".16", double* %"w"
  br label %"ifend"
else:
  %"z.3" = load double, double* %"z"
  %".19" = sitofp i32 5 to double
  %".20" = fsub double %"z.3", %".19"
  store double %".20", double* %"w"
  br label %"ifend"
ifend:
  %"w.1" = load double, double* %"w"
  %".23" = bitcast [4 x i8]* @"fstr_float" to i8*
  %".24" = call i32 (i8*, ...) @"printf"(i8* %".23", double %"w.1")
  ret i32 0
}

@"fstr_float" = internal constant [4 x i8] c"%f\0a\00"