import java.io.*;
import java.util.Scanner;

public class filehandle {
    public static void main(String[] args) {
        String filePath = "name.txt";
        File f=new File(filePath);
        try{
            Scanner sc=new Scanner(f);
            if(!sc.hasNext())
            {
                System.out.println("the folder is Empty"+filePath);
            }
            while (sc.hasNext()) {
                System.out.print(" "+sc.next());
            }
        }catch(Exception e)
        {
            System.out.println("404: file not found Error");
        }
    }
}