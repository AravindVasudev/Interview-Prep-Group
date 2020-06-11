public class RotateRight {
    public static void main(String agrs[]) {
        test(new int[] {1, 2, 3, 4, 5}, 2, new int[] {4 ,5 ,1 ,2 ,3});
        test(new int[] {1, 2, 3, 4, 5}, 0, new int[] {1, 2, 3, 4, 5});
        test(new int[] {1, 2, 3, 4, 5}, 5, new int[] {1, 2, 3, 4, 5});
        test(new int[] {1, 2, 3, 4, 5}, 10, new int[] {1, 2, 3, 4, 5});
        test(new int[] {1, 2, 3, 4, 5}, 4, new int[] {2, 3, 4, 5, 1});
        test(new int[] {1, 2, 3, 4, 5}, 3, new int[] {3, 4, 5, 1, 2});
        test(new int[] { }, 3, new int[] { });
    }

    private static void test(int[] input, int k, int[] exp) {
        Node inputList = formList(input);
        Node expList = formList(exp);

        // Rotate
        inputList = new Solution().rotateRight(inputList, k);
        System.out.print("RotatedList: ");
        print(inputList);
        System.out.print("ExpectedList: ");
        print(expList);
        System.out.println("-------------------------------------");
    }

    private static void print(Node n1) {
        while (n1 != null) {
            System.out.print(n1.val + " ");
            n1 = n1.next;
        }
        System.out.println();
    }

    private static Node formList(int[] arr) {
        Node head = new Node(0), node = head;
        for (int i = 0; i < arr.length; i++) {
            Node n = new Node(arr[i]);
            node.next = n;
            node = node.next;
        }
        return head.next;
    }
}

class Solution {
    public Node rotateRight (Node head, int k){

        int len = 0;
        Node itr = head;
        Node end = head;
        int rotate = k;

        while(itr != null) {
            end = itr;
            itr = itr.next;
            len++;
        }
        if(len == 0){
            return head;
        }

        rotate = k % len;
        if(rotate == 0)
            return head;
        itr = head;
        for(int i = 0; i < len - rotate - 1; i++){
            itr = itr.next;
        }

        Node newHead = itr.next;
        itr.next = null;
        end.next = head;
        
        return newHead;
    }
}

class Node {
    int val;
    Node next;

    Node(int val){
        this.val = val;
        this.next = null;
    }

    Node(int val, Node node){
        this.val = val;
        this.next = null;
    }
}