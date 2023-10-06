/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let a = 0;
    let i;
    for (i = 0; i < nums.length; i++) {
        let p = target - nums[i];
        if (nums.includes(p)) {
            a = nums.indexOf(p);
            if (a === i) {
                continue;
            }
            break;
        }
    }
    return [i, a];
};
