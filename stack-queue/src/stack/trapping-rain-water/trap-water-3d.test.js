import { waterTrapped } from './trap-water-3d.js'

describe("trap-water-4d", () => {
    test('with 3 rows', () => {
        const elevations = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
        const waterTrapped = trapWater3D(elevations)
        expect(waterTrapped).toBe(4)
    })
})