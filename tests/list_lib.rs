use leet::list_lib::Node;

#[test]
fn test_list_lib() {
    // Non recursive transformations
    // Trafo from vector to linked list
    let arr: Vec<u8> = vec![1, 3, 5, 7];
    let from_vec = Node::from_arr(arr.clone()).unwrap();
    
    // Trafo from node to vector
    let back_from_vec = Node::from_node(from_vec);

    // Reverse output vector
    let mut rev_from_vec = back_from_vec.clone();
    rev_from_vec.reverse();

    assert_eq!(arr, rev_from_vec);
}
