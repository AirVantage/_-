#!/usr/bin/python3
import fileinput
import re

SAME_IN_LODASH_AND_UNDERSCORE = [
  '_.bind',
  '_.clone',
  '_.compact',
  '_.constant',
  '_.defaults',
  '_.difference',
  '_.escape',
  '_.has',
  '_.includes',
  '_.intersection',
  '_.isArray',
  '_.isBoolean',
  '_.isDate',
  '_.isElement',
  '_.isEmpty',
  '_.isEqual',
  '_.isFunction',
  '_.isNaN',
  '_.isNull',
  '_.isNumber',
  '_.isObject',
  '_.isString',
  '_.isUndefined',
  '_.keys',
  '_.memoize',
  '_.mixin',
  '_.negate',
  '_.noop',
  '_.now',
  '_.partial',
  '_.property',
  '_.range',
  '_.result',
  '_.size',
  '_.toArray',
  '_.unescape',
  '_.union',
  '_.uniqueId',
  '_.values',
  '_.without',
]

CONVERTED_FROM_UNDERSCORE = {
  '_.all': ['_.every', '_.every(_.bind)'],
  '_.any': ['_.some', '_.some(_.bind)'],
  '_.contains': ['_.includes'],
  '_.debounce': ['_.debounce'],
  '_.detect': ['_.find', '_.find(_.bind)'],
  '_.each': ['_.forEach', '_.forEach(_.bind)'],
  '_.every': ['_.every(_.bind)'],
  '_.extend': ['_.assignIn'],
  '_.filter': ['_.filter', '_.filter(_.bind)'],
  '_.find': ['_.find', '_.find(_.bind)'],
  '_.findWhere': ['_.find'],
  '_.first': ['_.head', '_.take'],
  '_.flatten': ['_.flatten', '_.flattenDeep'],
  '_.forEach': ['_.forEach(_.bind)'],
  '_.get': ['_.get'],
  '_.groupBy': ['_.groupBy(_.bind)'],
  '_.include': ['_.includes'],
  '_.indexBy': ['_.keyBy', '_.keyBy(_.bind)'],
  '_.indexOf': ['_.indexOf', '_.sortedIndexOf'],
  '_.initial': ['_.dropRight', '_.initial'],
  '_.invoke': ['_.invokeMap'],
  '_.last': ['_.last', '_.takeRight'],
  '_.map': ['_.map', '_.map(_.bind)'],
  '_.mapObject': ['_.mapValues', '_.mapValues(_.bind)'],
  '_.max': ['_.last', '_.last(_.bind)'],
  '_.min': ['_.head', '_.head(_.bind)'],
  '_.object': ['_.zipObject'],
  '_.omit': ['_.omit', '_.omitBy'],
  '_.pairs': ['_.toPairs'],
  '_.pick': ['_.pick', '_.pickBy'],
  '_.pluck': ['_.map'],
  '_.reduce': ['_.reduce', '_.reduce(_.bind)'],
  '_.reject': ['_.reject', '_.reject(_.bind)'],
  '_.require': ['_.require'],
  '_.rest': ['_.drop'],
  '_.some': ['_.some', '_.some(_.bind)'],
  '_.sortBy': ['_.sortBy(_.bind)'],
  '_.times': ['_.times', '_.times(_.bind)'],
  '_.uniq': ['_.sortedUniq', '_.sortedUniqBy', '_.uniqBy'],
  '_.unique': ['_.sortedUniq', '_.sortedUniqBy', '_.uniqBy'],
  '_.where': ['_.filter'],
}

UNDERSCORE = CONVERTED_FROM_UNDERSCORE.keys()

CONVERTED_FROM_SIERRA = {
  '_.deep': ['_.get', '_.set'],
}

# Lodash functions used
LODASH = sum(CONVERTED_FROM_UNDERSCORE.values(), [])
LODASH += sum(CONVERTED_FROM_SIERRA.values(), [])
LODASH = sorted(LODASH)

#
# Process standard input
#
functions = {}
ansi_escape = re.compile(r'\x1b[^m]*m\n*')
processed_term = []
for term in fileinput.input():

  # Pass when work is already done
  if term in processed_term:
    continue
  else:
    processed_term += term

  # Trim standard input from color codes
  plain_term = ansi_escape.sub('', term)

  # Check function's conversion status
  conversions = CONVERTED_FROM_UNDERSCORE.get(plain_term)
  availableInUnderscore = plain_term in UNDERSCORE
  checks = {
    'conversions': conversions,
    'loash': plain_term in LODASH,
    'needs conversion': availableInUnderscore and conversions is None,
    'sierra': CONVERTED_FROM_SIERRA.get(plain_term),
    'transparent': plain_term in SAME_IN_LODASH_AND_UNDERSCORE,
    'underscore': availableInUnderscore
  }

  # Trim the useless
  checks = {k: v for k, v in checks.items() if v not in [None, False]}
  functions[plain_term] = checks

for functionName in sorted(functions.keys()):
  print(functionName)
  function = functions.get(functionName)
  for prop in sorted(function.keys()):
    print('\t{}: {}'.format(prop, function.get(prop)))
