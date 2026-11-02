class Solution {
    public boolean isPalindrome(String s) {
        String formatString = s.toLowerCase().replaceAll("[^0-9a-z]", "");
        int start = 0;
        int end = formatString.length() - 1;

        while (start <= end) {
            if (formatString.charAt(start) != formatString.charAt(end)) {
                return false;
            } else {
                start++;
                end--;
            }
        }

        return true;
    }
}
