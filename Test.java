import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.LinkedHashMap;
import java.util.Map;

public class Test {

    private Map<String, String> parseYangFile(String path) {
        BufferedReader reader;
        Map<String, String> yangNodeTypes = new LinkedHashMap<String, String>();

        try {
            reader = new BufferedReader(new FileReader(path));
            String line = reader.readLine();
            while (line != null){
                line = line.trim();
                String[] splitted = line.split(" ");
                if (splitted.length == 3 && splitted[2].equals("{") 
                && splitted[0].matches("container|leaf|leaf-list|list")) {
                    System.out.println(splitted[1] + " is of type " + splitted[0]);
                    yangNodeTypes.put(splitted[1], splitted[0]);
                    System.out.println("Added to map\n");
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
        
        return yangNodeTypes;
    } 

    public static void main(String[] args) {
        Test test = new Test();
        Map<String, String> yangNodeTypes = test.parseYangFile("yang/ietf-interfaces.yang");
    }
    
}
