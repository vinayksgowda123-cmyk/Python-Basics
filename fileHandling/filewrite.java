import java.io.*;
public class filewrite {

    public static void main(String[] args)
    {
        File f=new File("name.txt");

        try{
            FileWriter fw=new FileWriter(f);
            fw.write("Iam intoducing an Laxmi narayan ");
            fw.write("He is an good boy ");
            fw.write("He is the smartest boy in the class");
            fw.close();
        }catch(Exception e)
        {
            System.out.println(e.getMessage());
        }
    }
}
