class Solution {
    public boolean isAnagram(String s, String t) {
        char [] string_one = s.toCharArray();
        char [] string_two = t.toCharArray();

        Arrays.sort(string_one);
        Arrays.sort(string_two);

        String s_1 = new String(string_one);
        String s_2 = new String(string_two);

        return s_1.equals(s_2);
    }
}
