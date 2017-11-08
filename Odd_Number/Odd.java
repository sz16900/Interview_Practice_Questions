class Odd {
  void odd() {
    for (Integer i = 1; i < 100; i = i+2) {
      System.out.print(i + " ");
    }
    System.out.print("\n");
  }

  public static void main(String args[]) {
    Odd program = new Odd();
    program.odd();
  }
}
