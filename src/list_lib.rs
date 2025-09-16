// Linked list
pub struct Node {
    ele: u8,
    next: Option<Box<Node>>,
}

impl Node {
    pub fn con_struct(element: u8, next: Option<Box<Node>>) -> Self {
        Node {
            ele: element,
            next: next,
        }
    }

    pub fn from_arr(arr: Vec<u8>) -> Option<Box<Node>> {
        let mut node = None;

        for ele in arr {
            node = Some(Box::new(Node::con_struct(ele, node)));
        }

        return node
    }

    pub fn from_node(start_node: Box<Node>) -> Vec<u8> {
        // traverse in reverse order?
        let mut current = &Some(start_node);
        // Debug: println!("{}", current.as_ref().unwrap().ele);

        let mut arr: Vec<u8> = vec![];

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
}
