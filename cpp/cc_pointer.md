# Smart pointer

- added benefit over using raw pointers is automatic memory management of dynamically allocated resources, so that you don't have to make explicit calls to delete.

## Pointer versus Reference
- https://blog.csdn.net/tianxiaolu1175/article/details/46889523
- reference
```cpp
int real = 2;
int& ref = real;

std::vector<int> vec;
vec.push_back(real);
vec.push_back(ref); // will change together
```

## unique pointer
- Use a unique_ptr when an object claims ownership of a resource. That is, the object is responsible for managing the memory of the resource, deleting it when it's own destructor is called. Also, note that the assignment operator of a unique_ptr only accepts rvalues, which should be provided by std::move semantics.
```cpp
unique_ptr<T> abc;
abc.reset(new abc()); // has to be new, shouldn't be passed
abc.get();

// create
// e.g., unique_ptr<int> v1 = make_unique<int>(3);
auto instance = make_unique<T>(xxx);
auto instance = unique_ptr<T>(new T(xxx));
```

## rvalue reference and std::move
- rvalue reference &&
```cpp
// constructor
MyString(MyString&& str) {
 _len = str._len; _data = str._data;
}
```
- std::move(): used to indicate that an object t may be "moved from", i.e. allowing the efficient transfer of resources from t to another object. Always combined with **unique_ptr**
```cpp
std::move(T&& t);

std::string str = "Hello";
std::vector<std::string> v;
v.push_back(str); // str is still "Hello", a deep copy
v.push_back(std::move(str)); // str is now "", moved here
```

## shared_ptr
- Use a shared_ptr when you heap-allocate a resource that needs to be shared among multiple objects. It maintains a reference count internally and only deletes the resource when the reference count goes to zero.
```cpp
template< class T >
class shared_ptr;

// modifier
void reset() noexcept;
template <class Y> 
void reset(Y* ptr);
template <class Y, class Deleter> 
void reset(Y* ptr, Deleter d);
template <class Y, class Deleter, class Alloc> 
void reset( Y* ptr, Deleter d, Alloc alloc );

T* get();
```
- Don't use multiple shared_ptr pointing to a same raw pointer, otherwise problem when destruction.
```cpp
#include <memory>

auto p = shared_ptr<T>(new T(xxx));
auto p = make_shared<T>(xxx);

p.reset(new T());
p.reset();

std::cout << *p.get();
```