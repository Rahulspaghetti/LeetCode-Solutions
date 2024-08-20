class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int total_values = numbers.length;
        int left = 0;
        int right = total_values - 1;
        int sum = 0;
        int[] output = new int[2];

        while(left < total_values) {
            sum = numbers[left] + numbers[right];
            if (sum == target) {
                output[0] = left + 1;
                output[1] = right + 1;
                return output;
            }
            else if(sum < target){
                left++;
            }
            else {
                right--;
            }
            
        }
        return output;
    }
}