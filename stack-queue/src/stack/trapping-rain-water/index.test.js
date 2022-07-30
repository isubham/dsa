import { getBreakers, trapRainWater } from './index.js'

describe('getBreakers', () => {
     test('with valid 3 digit inputs', () => {
          const breakers = getBreakers([1, 0, 2])
          expect(breakers.value()).toEqual([{pos:0, elevation:1}, {pos:2, elevation:2}])         
     })

     test('with valid 3 digit inputs', () => {
          const breakers = getBreakers([2, 0, 1])
          expect(breakers.value()).toEqual([{pos:0, elevation:2}, {pos:2, elevation:1}])         
     })

     test('with valid 4 digit inputs, should remove the middle elements which are smaller', () => {
          const breakers = getBreakers([2, 0, 1, 3])
          expect(breakers.value()).toEqual([{pos:0, elevation:2}, {pos:3, elevation:3}])         
     })

     test('with valid 4 digit inputs, should remove the middle elements which are smaller', () => {
          const breakers = getBreakers([3, 0, 1, 4])
          expect(breakers.value()).toEqual([{pos:0, elevation:3}, {pos:3, elevation:4}])         
     })

     test('with increasing values', () => {
          const elevations = [1, 0, 2, 0, 4]
          const breakers = getBreakers(elevations)
          expect(breakers.value()).toEqual([{pos:0, elevation:1}, {pos:2, elevation:2}, {pos:4, elevation:4}])         
     })

     test('with increasing values then decreasing values', () => {
          const elevations = [1, 0, 2, 0, 1]
          const breakers = getBreakers(elevations)
          expect(breakers.value()).toEqual([{pos:0, elevation:1}, {pos:2, elevation:2}, {pos:4, elevation:1}])         
     })

     test('with increasing values then decreasing values', () => {
          const elevations = [1, 0, 2, 0, 1, 0, 2]
          const breakers = getBreakers(elevations)
          expect(breakers.value()).toEqual([{pos:0, elevation:1}, {pos:2, elevation:2}, {pos:6, elevation:2}])         
     })
})

describe('trapRainWater', () => {

    test('with any 2 element elevation map should return 0', () => {
        expect(trapRainWater([0, 0])).toBe(0)
        expect(trapRainWater([0, 1])).toBe(0)
        expect(trapRainWater([1, 0])).toBe(0)
        expect(trapRainWater([1, 1])).toBe(0)
    });

    test('with increasing [1, 0, 2] should return 1', () => {
         expect(trapRainWater([1, 0, 2])).toBe(1)
    });

    test('with decreasing [2, 0, 1] should return 1', () => {
         expect(trapRainWater([2, 0, 1])).toBe(1)
    });

    test('with increasing [1, 0, 2, 0, 4] should return 3', () => {
         expect(trapRainWater([1, 0, 2, 0, 4])).toBe(3)
    });

    //
    test('with increasing [1, 0, 2, 0, 1] should return 3', () => {
         expect(trapRainWater([1, 0, 2, 0, 4])).toBe(3)
    });

    test('with increasing  and decreasing [1, 0, 2, 0, 4] should return 3', () => {
         expect(trapRainWater([1, 0, 2, 0, 4, 0, 2, 0, 3])).toBe(10)
    });
    //
});