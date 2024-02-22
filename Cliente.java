import java.rmi.Naming;

public class Cliente {
    private static Interface a = null;

    public static void main(String[] args) {
        try {
            server = (Interface) Naming.lookup("rmi://127.0.0.1:11099/RMIInterface");
            System.out.println(server.time());
            System.out.println(server.serverIP());
            System.out.println(server.storeString(server.serverIP()));
            System.out.println(server.listString());
        }
        catch (Exception e) {
            System.out.println("Trouble: " + e);
        }
    }
}
