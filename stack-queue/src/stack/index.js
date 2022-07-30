/**
 * @author : 'subhamkumarchandrawansi@gmail.com',
 * 
 * @version 1.1
 * @description added pop method which returns popped element
 * @date 26 march, 2022
 * 
 * @version 1.0
 * @date : '21st feb, 2022'
 * 
 */
let Stack = function () {
  this._data = [];
}

Stack.prototype.length = 0;

Stack.prototype.push = function(data) {
  this._data.push(data);
  this.length += 1
}


Stack.prototype.pop = function() {
  const element = this.peek();
  this._data.pop();
  this.length -= 1
  return element;
}

Stack.prototype.peek = function() {
  return this._data[this._data.length - 1]
};

Stack.prototype.toString = function() {
  console.log('bottom', this._data,'top')
}

Stack.prototype.value = function() {
  return this._data;
}

export default Stack
export { Stack }


