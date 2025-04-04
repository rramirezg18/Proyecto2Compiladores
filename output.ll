; ModuleID = "main"
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  %".2" = bitcast [17 x i8]* @"str.494693010260577949" to i8*
  %".3" = bitcast [4 x i8]* @"fmt_string" to i8*
  %".4" = call i32 (i8*, ...) @"printf"(i8* %".3", i8* %".2")
  %"i" = alloca i32
  store i32 0, i32* %"i"
  br label %"for.cond"
for.cond:
  %"i.1" = load i32, i32* %"i"
  %".7" = icmp sle i32 %"i.1", 20
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

@"str.494693010260577949" = internal constant [17 x i8] c"contador con for\00"
@"fmt_string" = internal constant [4 x i8] c"%s\0a\00"
@"fmt_int" = internal constant [4 x i8] c"%d\0a\00"