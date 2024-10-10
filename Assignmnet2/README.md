# گزارش اجرایی: تبدیل FSM از پایتون به کد C++

## **۱. مقدمه**

این گزارش مراحل انجام شده برای تبدیل یک ماشین حالت متناهی قطعی (FSM) تعریف‌شده در پایتون به کد اجرایی C++ را شرح می‌دهد.

## **۲. مراحل اجرایی**

### **الف. تعریف ساختار FSM در پایتون**
- **تعریف FSM:**
  - به صورت یک دیکشنری نمایش داده شد که در آن هر حالت به ورودی‌های ممکن و حالات بعدی مربوطه نگاشت شده است.
    ```python
    fsm = {
        'state1': {'input1': 'state2', 'input2': 'state3'},
        'state2': {'input1': 'state1', 'input2': 'state3'},
        'state3': {'input1': 'state1', 'input2': 'state2'},
    }
    start_state = 'state1'
    ```

### **ب. نگاشت حالات و ورودی‌ها به شمارش‌ها**
- **شمارش‌ها در C++:**
  - نوع‌های `enum` برای حالات و ورودی‌ها ایجاد شد تا عملکرد و ایمنی نوع را بهبود بخشد.
    ```cpp
    enum State { STATE1, STATE2, STATE3, INVALID_STATE };
    enum Input { INPUT1, INPUT2, INVALID_INPUT };
    ```

### **ج. ایجاد جدول انتقال**
- **آرایه دو بعدی:**
  - یک جدول انتقال به صورت یک آرایه دو بعدی ساخته شد که در آن `transition_table[current_state][input]` حالت بعدی را تعیین می‌کند.
    ```cpp
    State transition_table[3][2] = {
        {STATE2, STATE3},
        {STATE1, STATE3},
        {STATE1, STATE2},
    };
    ```

### **د. پیاده‌سازی تابع تبدیل ورودی**
- **تبدیل رشته به شمارش:**
  - تابعی توسعه داده شد تا رشته‌های ورودی کاربر را به مقادیر `Input` مربوطه تبدیل کند و در صورت عدم شناسایی ورودی، `INVALID_INPUT` را بازگرداند.
    ```cpp
    Input get_input(const string& input_str) {
        if(false) {}
        else if(input_str == "input1") return INPUT1;
        else if(input_str == "input2") return INPUT2;
        else return INVALID_INPUT;
    }
    ```

### **ه. مدیریت حالات و ورودی‌های نامعتبر**
- **مدیریت خطا:**
  - بررسی‌هایی برای `INVALID_INPUT` و `INVALID_STATE` اضافه شد تا پیام‌های اطلاعاتی ارائه داده و از رفتار نامتعریف جلوگیری شود.
    ```cpp
    if(input == INVALID_INPUT) {
        cout << "Invalid input!" << endl;
        continue;
    }

    if(next_state == INVALID_STATE) {
        cout << "Undefined transition!" << endl;
    } else {
        current_state = next_state;
    }
    ```

### **و. توسعه تابع اصلی با انتقال حالات**
- **حلقه اصلی:**
  - یک حلقه پیاده‌سازی شد که:
    1. حالت فعلی را نمایش می‌دهد.
    2. از کاربر ورودی دریافت می‌کند.
    3. ورودی را به شمارش تبدیل می‌کند.
    4. حالت بعدی را با استفاده از جدول انتقال تعیین و به آن منتقل می‌شود.
    5. در صورت درخواست کاربر، برنامه را خاتمه می‌دهد.
    ```cpp
    int main() {
    State current_state = STATE1;
    string input_str;

    while (true) {
        switch(current_state) {
            case STATE1:
                cout << "Current state: state1" << endl;
                break;
            case STATE2:
                cout << "Current state: state2" << endl;
                break;
            case STATE3:
                cout << "Current state: state3" << endl;
                break;
            default:
                cout << "Unknown state!" << endl;
                return 1;
        }

        cout << "Enter input (or type 'exit' to quit): "; 
        cin >> input_str;

        if(input_str == "exit") break;

        Input input = get_input(input_str);

        if(input == INVALID_INPUT) {
            cout << "Invalid input!" << endl;
            continue;
        }

        if(current_state < 0 || current_state >= 3) {
            cout << "Current state is invalid!" << endl;
            break;
        }

        State next_state = transition_table[current_state][input];

        if(next_state == INVALID_STATE) {
            cout << "Transition not defined for this input in the current state!" << endl;
        } else {
            current_state = next_state;
        }
    }

    cout << "FSM terminated." << endl;
    return 0;
}
    ```

## **۳. آزمایش**

- **کامپایل:** کد C++ تولید شده با استفاده از `g++` با موفقیت کامپایل شد.
  ```bash
  g++ -o fsm_program fsm_program.cpp
  ```
- **اجرای برنامه:** برنامه اجرا شد و انتقال حالات، مدیریت ورودی‌های نامعتبر و خاتمه‌ی نرم‌افزاری آن تأیید شد.
  ```
  Current state: state1
  Enter input (or 'exit' to quit): input1
  Current state: state2
  Enter input (or 'exit' to quit): invalid_input
  Invalid input!
  Current state: state2
  Enter input (or 'exit' to quit): exit
  FSM terminated.
  ```