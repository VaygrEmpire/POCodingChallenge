import scala.io.StdIn._

object GetVoteCount {

  def main(args:Array[String]):Unit = {
    //  Given an object containing counts of both upvotes and downvotes, return what vote count should be displayed.
    //  This is calculated by subtracting the number of downvotes from upvotes.
    //
    //  Examples
    //
    //  getVoteCount({upvotes: 13, downvotes: 0}) ➞ 13
    //  getVoteCount({upvotes: 2, downvotes: 33}) ➞ -31
    //  getVoteCount({upvotes: 132, downvotes: 132}) ➞ 0
    //
    //  Notes
    //  You can expect only positive integersfor vote counts.

    val voteDict1 = Map("upvotes" -> 13, "downvotes" -> 0)
    val voteDict2 = Map("upvotes" -> 2, "downvotes" -> 33)
    val voteDict3 = Map("upvotes" -> 132, "downvotes" -> 132)

    println(getVoteCount(voteDict1))
    println(getVoteCount(voteDict2))
    println(getVoteCount(voteDict3))

    def getVoteCount(votes: Map[String, Int]): Int = {
      votes("upvotes") - votes("downvotes")
    }
  }
}
