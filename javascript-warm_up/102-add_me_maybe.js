#!/usr/bin/node
exports.addMaybe = function (number, theFunction) {
  theFunction(++number);
};
