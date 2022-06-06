# ----------------------------------------------------------------------------
# Copyright (c) 2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from qiime2.plugin import SemanticType

StatsTable = SemanticType('StatsTable', field_names=['kind'])

Pairwise = SemanticType('Pairwise', variant_of=StatsTable.field['kind'])
