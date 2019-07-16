class Solution
{
public:
    void push(int node){
            stack1.push(node)
        }
    int pop(){
        if(stack2.empty())
        {
            while(!stack1.empty())
            {
                stack2.push(stack1.top());
                stack1.pop();
            }
        }
        else
        {
            temp=stack2.pop();
            stack2.pop();
            return temp;
        }
    }
private:
    stack<int> stack1;
    stack<int> stack2;
    int temp;
}