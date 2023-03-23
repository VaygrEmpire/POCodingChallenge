import scala.io.StdIn._

object TriangleArea {

  def main(args:Array[String]):Unit = {
//    Create a function that returns true when x is equal to y;
//    otherwise return false.

//    Examples
//    isSameNum(4, 8) ➞ false
//    isSameNum(2, 2) ➞ true
//    isSameNum(42, 32) ➞ false
//    Notes: Don't forget to return the result.

    val a = readLine("Please enter first number: ").toInt
    val b = readLine("Please enter second number: ").toInt
    println(isSameNum(a, b))
  }

  def isSameNum(x: Int, y: Int): Boolean = {
    if (x == y) { true } else { false }
  }

}
