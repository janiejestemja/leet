use leet::add;
use leet::list_lib::Node;
use leet::msort;

fn main() {
    println!("works?");
    println!("{}", add(11, 13));

    let arr: Vec<i32> = vec![11, 5, 3, 7, 13, 9, 0];
    let res = msort(arr);
    println!("{:?}", res);
}

fn old_main() {
    let arra: Vec<char> = vec![
        1 as char, 
        3 as char, 
        5 as char,
        7 as char
    ];
    let afrom_vec = Node::from_arr(arra.clone()).unwrap();
    
    // Trafo from node to vector
    let back_from_vec = Node::from_node(afrom_vec.clone());

    // Reverse output vector
    let mut rev_from_vec = back_from_vec.clone();
    rev_from_vec.reverse();

    assert_eq!(arra, rev_from_vec);

    let arrb: Vec<char> = vec![
        1 as char, 
        1 as char
    ];
    let bfrom_vec = Node::from_arr(arrb.clone()).unwrap();
    let sum = Node::ladd(Some(afrom_vec.clone()), Some(bfrom_vec.clone()));

    let l1: Vec<char> = vec![
        9 as char, 
        9 as char, 
        9 as char, 
        9 as char, 
        9 as char, 
        9 as char, 
        9 as char, 
        /*
        0 as char, 
        2 as char,
        4 as char,
        3 as char,
        */
    ];
    let l2: Vec<char>= vec![
        9 as char, 
        9 as char, 
        9 as char, 
        9 as char, 
        /*
        0 as char, 
        5 as char, 
        6 as char, 
        4 as char, 
        */
    ];
    let out: Vec<char> = vec![
        8 as char, 
        9 as char, 
        9 as char, 
        9 as char, 
        0 as char, 
        0 as char, 
        0 as char, 
        1 as char, 
        /*
        7 as char,
        0 as char, 
        8 as char, 
        */
    ];
    let afrom_vec = Node::from_arr(l1.clone()).unwrap();
    let bfrom_vec = Node::from_arr(l2.clone()).unwrap();
    let sum = Node::ladd(Some(afrom_vec.clone()), Some(bfrom_vec.clone()));
    let sum_arr = Node::from_node(sum.clone().unwrap());

    // Reverse output vector
    let mut rev_sum_arr = sum_arr.clone();
    rev_sum_arr.reverse();

    assert_eq!(arra, rev_from_vec);
    println!("Expexted: {:?}", out);
    println!("Nodes: {:?}", sum);
    println!("Array: {:?}", sum_arr);
    println!("Reversed Array: {:?}", rev_sum_arr);
}
