class Gt {

  Integer gt() {
    for (Integer i = 1; i < 13; i++) {
      for (Integer j = 1; j < 13; j++) {
        System.out.print(String.format("%4d", j * i ));
      }
      System.out.println(' ');
    }
    return 0;
  }

  public static void main (String args[]){
    Gt program = new Gt();
    program.gt();
  }

}
