import { LoremFormat } from "./constants/formats";
import { LoremUnit } from "./constants/units";
import { IPrng } from "./lib/generator";
import LoremIpsum from "./lib/LoremIpsum";
export interface ILoremIpsumParams {
    count?: number;
    format?: LoremFormat;
    paragraphLowerBound?: number;
    paragraphUpperBound?: number;
    random?: IPrng;
    sentenceLowerBound?: number;
    sentenceUpperBound?: number;
    units?: LoremUnit;
    words?: string[];
    suffix?: string;
}
declare const loremIpsum: ({ count, format, paragraphLowerBound, paragraphUpperBound, random, sentenceLowerBound, sentenceUpperBound, units, words, suffix, }?: ILoremIpsumParams) => string;
export { loremIpsum, LoremIpsum };
