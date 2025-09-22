pub mod list_lib;

pub fn add(left: u64, right: u64) -> u64 {
    left + right
}

pub fn msort(arr: Vec<i32>) -> Vec<i32> {
    if arr.len() == 1 {return arr}
    let piv: usize = arr.len() / 2;
    
    let left: Vec<i32> = msort(arr[0..piv].to_vec());
    let right: Vec<i32> = msort(arr[piv..].to_vec());
    merge(left, right)
}

pub fn merge(left: Vec<i32>, right: Vec<i32>) -> Vec<i32> {
    let mut i = 0;
    let mut j = 0;

    let mut sorted: Vec<i32> = vec![];
    while i < left.len() && j < right.len() {

        if left[i] <= right[j] {
            sorted.push(left[i].clone());
            i += 1;
        } else { 
            sorted.push(right[j].clone());
            j += 1;
        }
    }

    for ele in left[i..].iter() {
        sorted.push(ele.clone())
    }
    for ele in right[j..].iter() {
        sorted.push(ele.clone())
    }
    sorted
}
