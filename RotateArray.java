c int[] rotate(int[] nums, int k) {
        k = k % nums.length;
        if(nums == null || k < 0) throw new IllegalArgumentException("Illegal argument!");
        int len = nums.length;
        int half = len - k;
        reverse(nums, 0, half-1);
        reverse(nums, half, len -1);
        reverse(nums, 0, len -1);
        return nums;
    }
    public void reverse (int[] nums, int l, int r) {
        if (nums == null || nums.length == 1) return;
        while(l < r) {
            int temp = nums[l];
            nums[l] = nums[r];
            nums[r] = temp;
            l++;
            r--;
        }
    }
