pub mod list_lib;

pub fn add(left: u64, right: u64) -> u64 {
    left + right
}

pub fn msort(arr: Option<Vec<i32>>) -> Option<Vec<i32>> {
    let arr = arr?;
    if arr.len() == 1 {return Some(arr)}
    let piv: usize = arr.len() / 2;
    
    let left: Option<Vec<i32>> = msort(Some(arr[0..piv].to_vec()));
    let right: Option<Vec<i32>> = msort(Some(arr[piv..].to_vec()));
    Some(merge(left, right)?)
}

pub fn merge(left: Option<Vec<i32>>, right: Option<Vec<i32>>) -> Option<Vec<i32>> {
    let mut i = 0;
    let mut j = 0;

    let left = left?;
    let right = right?;

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
    Some(sorted)
}
