#fundamentals 
When passing a _mutable_ object, Python passes the object reference, allowing any mutating methods to mutate the object directly. 

When passing _immutable_ objects, Python passes the value of the object, which doesn't give mutating methods full access to the object stored in memory and therefore doesn't allow for it to be mutated. 