using System;

public class LargestTwo
{
  public static int[] TwoOldestAges(int[] ages)
  {
    int[] xxx = new int[ages.Length];
    Array.Copy(ages, xxx, ages.Length);
    Array.Sort(xxx);
    return new int[]{xxx[xxx.Length-2], xxx[xxx.Length-1]};
  }
}
