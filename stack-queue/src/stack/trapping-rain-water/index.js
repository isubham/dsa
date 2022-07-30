import Stack from "..";

export const getBreakers = (elevations) => {

    let breakers = new Stack();
    for (let i = 0; i < elevations.length; i++) {
        let elevation = elevations[i];

        if (elevation == 0) {
            continue;
        }

        const currentElevation = {pos: i, elevation: elevation}

        // fills 2 breakers if it is non-empty
        if (breakers.length < 2 && elevation > 0 ) {
            breakers.push(currentElevation);
        }

        else {

            const lastElementIsLowerThanCurrentElevation = () => {
                const isTrue = breakers.peek().elevation < elevation
                return isTrue;
            } 

            const ishavingMoreThanOneElementAnd = () => {
                const isTrue = breakers.length > 1 
                return isTrue;
            }


            const popOnlyIfElementIsLessThanItsPrevious = () => {
                let popped = false;

                const elementPopped = breakers.pop();
                popped = true;

                if (elementPopped.elevation > breakers.peek().elevation) {
                    breakers.push(elementPopped)
                    popped = false;
                }
                return popped;
            }

            let popped = true;
            while (ishavingMoreThanOneElementAnd() && lastElementIsLowerThanCurrentElevation() && popped) {
                popped = popOnlyIfElementIsLessThanItsPrevious()
            }

            if (popped || lastElementIsLowerThanCurrentElevation()) {
                breakers.push(currentElevation);
            }
        }
        

    }
    return breakers;
}

const trapRainWater = (elevations) => {

    if (elevations.length < 3) {
        return 0
    }

    const breakers = getBreakers(elevations);
    console.log(`breakers`, breakers.toString())
    let totalWaterFilled = 0;

    let {pos, elevation} = breakers.pop();
    while(breakers.length > 0) {
        const {pos: posLeftSide, elevation: elevationLeftSide} = breakers.pop();
        const waterLevel = Math.min(elevation, elevationLeftSide);
        for (let i = posLeftSide + 1; i < pos; i++) {
            const elevationAtPos = elevations[i];
            const waterToBeFilledAtPos = waterLevel - elevationAtPos;
            totalWaterFilled += waterToBeFilledAtPos
        }

        pos = posLeftSide; elevation = elevationLeftSide;
    }

    return totalWaterFilled;

};

export { trapRainWater };
