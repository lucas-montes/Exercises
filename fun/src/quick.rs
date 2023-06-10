pub fn quicksort(arr: &mut [usize]) {
    // Base case: If the array is empty or contains only one element, it is already sorted
    if arr.len() <= 1 {
        return;
    }

    // Choose a pivot element (here, we choose the last element of the array)
    let pivot = arr[arr.len() - 1];

    // Partition the array into two halves based on the pivot
    let mut i = 0;
    for j in 0..arr.len() - 1 {
        if arr[j] <= pivot {
            arr.swap(i, j);
            i += 1;
        }
    }

    // Place the pivot in its correct position by swapping it with the element at index i
    arr.swap(i, arr.len() - 1);

    // Recursively apply quicksort to the left and right subarrays
    let (left, right) = arr.split_at_mut(i);
    quicksort(left);
    quicksort(&mut right[1..]);
}

