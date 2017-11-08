class Reverse_String {

    String reversed_string(String the_string) {
    	String reversed_string = "";
    	for (int i = the_string.length()-1; i >= 0; i--) {
    		reversed_string = reversed_string + the_string.charAt(i);
    	}
    	return reversed_string;
    }

    public static void main(String[] args) {
        Reverse_String program = new Reverse_String();         
        System.out.println(program.reversed_string(args[0]));
    }
}