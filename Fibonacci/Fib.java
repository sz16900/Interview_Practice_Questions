class Fib {

	Integer fibonacci(Integer n) {
		if (n == 0) {
			return 0;
		}
		else if (n == 1) {
			return 1;
		}
		else {
			return (fibonacci(n-1)) + (fibonacci(n-2));
		}
	}

	public static void main(String args[]) {
		Fib program = new Fib();
		for (Integer i = 0; i<=10; i++) {
			System.out.println(program.fibonacci(i));
		}
	}
}