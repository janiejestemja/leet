// Linked list
#[derive(Clone, Debug)]
pub struct Node {
    ele: char,
    next: Option<Box<Node>>,
}

impl Node {
    pub fn from_arr(arr: Vec<char>) -> Option<Box<Node>> {
        let mut node = None;

        for ele in arr {
            node = Some(Box::new(Node {
                ele: ele, 
                next: node
            }));
        }

        return node
    }

    pub fn from_node(start_node: Box<Node>) -> Vec<char> {
        // traverse in reverse order?
        let mut current = &Some(start_node);
        // Debug: println!("{}", current.as_ref().unwrap().ele);

        let mut arr: Vec<char> = vec![];

        // no idea why this works...
        while let Some(node) = current {
            // Debug: println!("{}", node.ele);
            arr.push(node.ele);

            if node.next.is_none() {
                break
            } else {
                current = &node.next;
            }
        }
        arr
    }

    pub fn ladd(left: Option<Box<Node>>, right: Option<Box<Node>>) -> Option<Box<Node>> {
        // setup solution
        let mut sol: usize = 0;
        let mut expon: usize = 1;

        // no idea why this works... fixed, kind of?
        let mut node = left.as_ref().unwrap();
        loop {
            // Debug: println!("{}", node.ele);
            sol += (node.ele as usize) * expon;
            expon *= 10;

            if node.next.is_none() {
                break
            } else {
                node = node.next.as_ref().unwrap();
            }
        }

        // reset exponent
        expon = 1;
        let mut node = right.as_ref().unwrap();
        loop {
            // Debug: println!("{}", node.ele);
            sol += (node.ele as usize) * expon;
            expon *= 10;

            if node.next.is_none() {
                break
            } else {
                node = node.next.as_ref().unwrap();
            }
        }

        // Convert to string then linked list
        let sol_str: String = sol.to_string();
        let mut node: Option<Box<Node>> = None;
        for i in 0..sol_str.len() {
            let cha = sol_str.chars().nth(i).unwrap();
            node = Some(Box::new(Node {
                ele: cha as char,
                next: node
            }));

        }

        node
    }
}
