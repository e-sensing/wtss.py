#
#   Copyright (C) 2014 National Institute For Space Research (INPE) - Brazil.
#
#  This file is part of Python Client API for Web Time Series Service.
#
#  Web Time Series Service for Python is free software: you can
#  redistribute it and/or modify it under the terms of the
#  GNU Lesser General Public License as published by
#  the Free Software Foundation, either version 3 of the License,
#  or (at your option) any later version.
#
#  Web Time Series Service for Python is distributed in the hope that
#  it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Web Time Series Service for Python. See LICENSE. If not, write to
#  e-sensing team at <esensning-team@dpi.inpe.br>.
#

from wtss import wtss

w = wtss("http://www.dpi.inpe.br/tws")

cv_list = w.list_coverages()

print(cv_list)

cv_scheme = w.describe_coverage("mod13q1_512")

print(cv_scheme)

ts = w.time_series("mod13q1_512", ["red", "nir"], -12.0, -54.0, "", "")

print(ts)

