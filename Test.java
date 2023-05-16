import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class Test {

    private void parseYangFile(String path) {
        BufferedReader reader;

        try {
            reader = new BufferedReader(new FileReader(path));
            String line = reader.readLine();
            while (line != null){
                line = line.trim();
                String[] splitted = line.split(" ");
                if (splitted.length == 3 && splitted[2].equals("{") 
                && splitted[0].matches("container|leaf|leaf-list|list")) {
                    System.out.println(splitted[1] + " is of type " + splitted[0]);
                }
                line = reader.readLine();
        }
        } catch (FileNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        
    } 

    public static void main(String[] args) {
        Test test = new Test();
        test.parseYangFile("yang/ietf-interfaces.yang");
    }
    
}
