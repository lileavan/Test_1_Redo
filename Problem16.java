import java.util.*;
class Problem16{
  public static void main(String[]args){
     Scanner scan= new Scanner(System.in);
  String str= "/* comment */";
  checkMulti(str);
  }
  static void checkMulti(String str){
    String[] split = str.split("*/");
    for(int i = 0;i<split.length;i++){
      System.out.print(split[i]);
      if(!(split[i].charAt(0)=='/' && split[i].charAt(1)=='*'))
        System.out.print("This is not a valid multiline comment");
    }
    System.out.print("This is a Valid multiline comment");
    
  }
}