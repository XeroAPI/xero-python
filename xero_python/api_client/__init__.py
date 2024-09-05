# coding: utf-8
"""
    Xero oAuth 2 identity service

    This specifing endpoints related to managing authentication tokens and identity for Xero API  # noqa: E501

    OpenAPI spec version: 2.0.4
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import datetime
import json
import mimetypes
import os
import re
import tempfile
from decimal import Decimal
from multiprocessing.pool import ThreadPool
from urllib.parse import quote

import xero_python
from xero_python import rest
from xero_python.api_client.configuration import Configuration
from xero_python.api_client.deserializer import deserialize
from xero_python.api_client.serializer import serialize
from xero_python.exceptions import OAuth2TokenGetterError, OAuth2TokenSaverError


class ModelFinder:
    """
    Model finder to find correct model class for given model name
    """

    def __init__(self, models_module):
        self.models = models_module

    def find_model(self, name):
        return getattr(self.models, name)


class ApiClient(object):
    """Generic API client for OpenAPI client library builds.

    OpenAPI generic API client. This client handles the client-
    server communication, and is invariant across implementations. Specifics of
    the methods and models for each application are generated from the OpenAPI
    templates.

    NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech
    Do not edit the class manually.

    :param configuration: .Configuration object for this client
    :param header_name: a header to pass when making calls to the API.
    :param header_value: a header value to pass when making calls to
        the API.
    :param cookie: a cookie to include in the header when making calls
        to the API
    :param pool_threads: The number of threads to use for async requests
        to the API. More threads means more concurrent API requests.
    """

    PRIMITIVE_TYPES = (float, bool, bytes, str, int)
    NATIVE_TYPES_MAPPING = {
        "int": int,
        "long": int,
        "float": float,
        "str": str,
        "bool": bool,
        "date": datetime.date,
        "datetime": datetime.datetime,
        "object": object,
    }
    _pool = None

    def __init__(
        self,
        configuration=None,
        header_name=None,
        header_value=None,
        cookie=None,
        pool_threads=None,
        oauth2_token_saver=None,
        oauth2_token_getter=None,
    ):
        if configuration is None:
            configuration = Configuration()
        self.configuration = configuration
        self.pool_threads = pool_threads

        self.rest_client = rest.RESTClientObject(configuration)
        self.default_headers = {}
        if header_name is not None:
            self.default_headers[header_name] = header_value
        self.cookie = cookie
        # Set default User-Agent.
        self.user_agent = "xero-python ({version})".format(
            version=xero_python.__version__
        )
        self._oauth2_token_saver = oauth2_token_saver
        self._oauth2_token_getter = oauth2_token_getter

    def __del__(self):
        if self._pool:
            self._pool.close()
            self._pool.join()
            self._pool = None

    @property
    def pool(self):
        """Create thread pool on first request
        avoids instantiating unused threadpool for blocking clients.
        """
        if self._pool is None:
            self._pool = ThreadPool(self.pool_threads)
        return self._pool

    @property
    def user_agent(self):
        """User agent for this API client"""
        return self.default_headers["User-Agent"]

    @user_agent.setter
    def user_agent(self, value):
        self.default_headers["User-Agent"] = value

    def set_default_header(self, header_name, header_value):
        self.default_headers[header_name] = header_value

    def __call_api(
        self,
        resource_path,
        method,
        path_params=None,
        query_params=None,
        header_params=None,
        body=None,
        post_params=None,
        files=None,
        response_type=None,
        response_model_finder=None,
        auth_settings=None,
        _return_http_data_only=None,
        collection_formats=None,
        _preload_content=True,
        _request_timeout=None,
    ):
        config = self.configuration

        # header parameters
        header_params = header_params or {}
        header_params.update(self.default_headers)
        if self.cookie:
            header_params["Cookie"] = self.cookie
        if header_params:
            header_params = serialize(header_params)
            header_params = dict(
                self.parameters_to_tuples(header_params, collection_formats)
            )

        # path parameters
        if path_params:
            path_params = serialize(path_params)
            path_params = self.parameters_to_tuples(path_params, collection_formats)
            for k, v in path_params:
                # specified safe chars, encode everything
                resource_path = resource_path.replace(
                    "{%s}" % k, quote(str(v), safe=config.safe_chars_for_path_param)
                )

        # query parameters
        if query_params:
            query_params = serialize(query_params)
            query_params = self.parameters_to_tuples(query_params, collection_formats)

        # post parameters
        if post_params or files:
            post_params = self.prepare_post_parameters(post_params, files)
            post_params = serialize(post_params)
            post_params = self.parameters_to_tuples(post_params, collection_formats)

        # auth setting
        self.update_params_for_auth(header_params, query_params, auth_settings)

        # body
        if body:
            body = serialize(body)

        # request url
        url = resource_path

        # perform request and return response
        response_data = self.request(
            method,
            url,
            query_params=query_params,
            headers=header_params,
            post_params=post_params,
            body=body,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
        )

        self.last_response = response_data

        return_data = response_data
        if _preload_content:
            # deserialize response data
            if response_type:
                return_data = self.deserialize(
                    response_data, response_type, response_model_finder
                )
            else:
                return_data = None

        if _return_http_data_only:
            return return_data
        else:
            return (return_data, response_data.status, response_data.getheaders())

    def deserialize(self, response, response_type, response_model_finder):
        """Deserializes response into an object.

        :param response: RESTResponse object to be deserialized.
        :param response_type: class literal for
            deserialized object, or string of class name.
        :param response_model_finder: ModelFinder instance to find class for
            response_type class literal

        :return: deserialized object.
        """
        # handle file downloading
        # save response body into a tmp file and return the instance
        if response_type == "file":
            return self.__deserialize_file(response)

        # fetch data from response object
        try:
            data = json.loads(response.text, parse_float=Decimal)
        except ValueError:
            data = response.data

        return deserialize(response_type, data, response_model_finder)

    def __deserialize(self, data, klass, model_finder):
        """Deserializes dict, list, str into an object.

        :param data: dict, list or str.
        :param klass: class literal, or string of class name.
        :param model_finder: ModelFinder instance to find class for
            response_type class literal

        :return: object.
        """
        # TODO obsolete, remove
        if data is None:
            return None

        if isinstance(klass, str):
            if klass.startswith("list["):
                sub_kls = re.match(r"list\[(.*)\]", klass).group(1)
                return [
                    self.__deserialize(sub_data, sub_kls, model_finder)
                    for sub_data in data
                ]

            if klass.startswith("dict("):
                sub_kls = re.match(r"dict\(([^,]*), (.*)\)", klass).group(2)
                return {
                    k: self.__deserialize(v, sub_kls, model_finder)
                    for k, v in data.items()
                }

            # convert str to class
            if klass in self.NATIVE_TYPES_MAPPING:
                klass = self.NATIVE_TYPES_MAPPING[klass]
            else:
                klass = model_finder.find_model(klass)

        if klass in self.PRIMITIVE_TYPES:
            return self.__deserialize_primitive(data, klass, model_finder)
        elif klass == object:
            return self.__deserialize_object(data)
        elif klass == datetime.date:
            return self.__deserialize_date(data)
        elif klass == datetime.datetime:
            return self.__deserialize_datatime(data)
        else:
            return self.__deserialize_model(data, klass, model_finder)

    def call_api(
        self,
        resource_path,
        method,
        path_params=None,
        query_params=None,
        header_params=None,
        body=None,
        post_params=None,
        files=None,
        response_type=None,
        response_model_finder=None,
        auth_settings=None,
        async_req=None,
        _return_http_data_only=None,
        collection_formats=None,
        _preload_content=True,
        _request_timeout=None,
    ):
        """Makes the HTTP request (synchronous) and returns deserialized data.

        To make an async_req request, set the async_req parameter.

        :param resource_path: Path to method endpoint.
        :param method: Method to call.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be
            placed in the request header.
        :param body: Request body.
        :param post_params dict: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param auth_settings list: Auth Settings names for the request.
        :param response: Response data type.
        :param files dict: key -> filename, value -> filepath,
            for `multipart/form-data`.
        :param async_req bool: execute request asynchronously
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param collection_formats: dict of collection formats for path, query,
            header, and post parameters.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return:
            If async_req parameter is True,
            the request will be called asynchronously.
            The method will return the request thread.
            If parameter async_req is False or missing,
            then the method will return the response directly.
        """
        if not async_req:
            return self.__call_api(
                resource_path,
                method,
                path_params,
                query_params,
                header_params,
                body,
                post_params,
                files,
                response_type,
                response_model_finder,
                auth_settings,
                _return_http_data_only,
                collection_formats,
                _preload_content,
                _request_timeout,
            )
        else:
            thread = self.pool.apply_async(
                self.__call_api,
                (
                    resource_path,
                    method,
                    path_params,
                    query_params,
                    header_params,
                    body,
                    post_params,
                    files,
                    response_type,
                    response_model_finder,
                    auth_settings,
                    _return_http_data_only,
                    collection_formats,
                    _preload_content,
                    _request_timeout,
                ),
            )
        return thread

    def request(
        self,
        method,
        url,
        query_params=None,
        headers=None,
        post_params=None,
        body=None,
        _preload_content=True,
        _request_timeout=None,
    ):
        """Makes the HTTP request using RESTClient."""
        if method == "GET":
            return self.rest_client.GET(
                url,
                query_params=query_params,
                _preload_content=_preload_content,
                _request_timeout=_request_timeout,
                headers=headers,
            )
        elif method == "HEAD":
            return self.rest_client.HEAD(
                url,
                query_params=query_params,
                _preload_content=_preload_content,
                _request_timeout=_request_timeout,
                headers=headers,
            )
        elif method == "OPTIONS":
            return self.rest_client.OPTIONS(
                url,
                query_params=query_params,
                headers=headers,
                post_params=post_params,
                _preload_content=_preload_content,
                _request_timeout=_request_timeout,
                body=body,
            )
        elif method == "POST":
            return self.rest_client.POST(
                url,
                query_params=query_params,
                headers=headers,
                post_params=post_params,
                _preload_content=_preload_content,
                _request_timeout=_request_timeout,
                body=body,
            )
        elif method == "PUT":
            return self.rest_client.PUT(
                url,
                query_params=query_params,
                headers=headers,
                post_params=post_params,
                _preload_content=_preload_content,
                _request_timeout=_request_timeout,
                body=body,
            )
        elif method == "PATCH":
            return self.rest_client.PATCH(
                url,
                query_params=query_params,
                headers=headers,
                post_params=post_params,
                _preload_content=_preload_content,
                _request_timeout=_request_timeout,
                body=body,
            )
        elif method == "DELETE":
            return self.rest_client.DELETE(
                url,
                query_params=query_params,
                headers=headers,
                _preload_content=_preload_content,
                _request_timeout=_request_timeout,
                body=body,
            )
        else:
            raise ValueError(
                "http method must be `GET`, `HEAD`, `OPTIONS`,"
                " `POST`, `PATCH`, `PUT` or `DELETE`."
            )

    def parameters_to_tuples(self, params, collection_formats):
        """Get parameters as list of tuples, formatting collections.

        :param params: Parameters as dict or list of two-tuples
        :param dict collection_formats: Parameter collection formats
        :return: Parameters as list of tuples, collections formatted
        """
        new_params = []
        if collection_formats is None:
            collection_formats = {}
        for k, v in (
            params.items() if isinstance(params, dict) else params
        ):  # noqa: E501
            if k in collection_formats:
                collection_format = collection_formats[k]
                if collection_format == "multi":
                    new_params.extend((k, value) for value in v)
                else:
                    if collection_format == "ssv":
                        delimiter = " "
                    elif collection_format == "tsv":
                        delimiter = "\t"
                    elif collection_format == "pipes":
                        delimiter = "|"
                    else:  # csv is the default
                        delimiter = ","
                    new_params.append((k, delimiter.join(str(value) for value in v)))
            else:
                new_params.append((k, v))
        return new_params

    def prepare_post_parameters(self, post_params=None, files=None):
        """Builds form parameters.

        :param post_params: Normal form parameters.
        :param files: File parameters.
        :return: Form parameters with files.
        """
        params = []

        if post_params:
            params = post_params

        if files:
            for k, v in files.items():
                if not v:
                    continue
                file_names = v if type(v) is list else [v]
                for n in file_names:
                    with open(n, "rb") as f:
                        filename = os.path.basename(f.name)
                        filedata = f.read()
                        mimetype = (
                            mimetypes.guess_type(filename)[0]
                            or "application/octet-stream"
                        )
                        params.append(tuple([k, tuple([filename, filedata, mimetype])]))

        return params

    def select_header_accept(self, accepts):
        """Returns `Accept` based on an array of accepts provided.

        :param accepts: List of headers.
        :return: Accept (e.g. application/json).
        """
        if not accepts:
            return

        accepts = [x.lower() for x in accepts]

        if "application/json" in accepts:
            return "application/json"
        else:
            return ", ".join(accepts)

    def select_header_content_type(self, content_types):
        """Returns `Content-Type` based on an array of content_types provided.

        :param content_types: List of content-types.
        :return: Content-Type (e.g. application/json).
        """
        if not content_types:
            return "application/json"

        content_types = [x.lower() for x in content_types]

        if "application/json" in content_types or "*/*" in content_types:
            return "application/json"
        else:
            return content_types[0]

    def update_params_for_auth(self, headers, querys, auth_settings):
        """Updates header and query params based on authentication setting.

        :param headers: Header parameters dict to be updated.
        :param querys: Query parameters tuple list to be updated.
        :param auth_settings: Authentication setting identifiers list.
        """
        if not auth_settings:
            return

        for auth in auth_settings:
            auth_setting = self.configuration.auth_settings(auth)
            if callable(auth_setting):
                # some auth settings may need http client (eg. auth2 refresh token flow)
                auth_setting = auth_setting(api_client=self)
            if auth_setting:
                if not auth_setting["value"]:
                    continue
                elif auth_setting["in"] == "header":
                    headers[auth_setting["key"]] = auth_setting["value"]
                elif auth_setting["in"] == "query":
                    querys.append((auth_setting["key"], auth_setting["value"]))
                else:
                    raise ValueError(
                        "Authentication token must be in `query` or `header`"
                    )

    def __deserialize_file(self, response):
        """Deserializes body to file

        Saves response body into a file in a temporary folder,
        using the filename from the `Content-Disposition` header if provided.

        :param response:  RESTResponse.
        :return: file path.
        """
        fd, path = tempfile.mkstemp(dir=self.configuration.temp_folder_path)
        os.close(fd)
        os.remove(path)

        content_disposition = response.getheader("Content-Disposition")
        if content_disposition:
            filename = re.search(
                r'filename=[\'"]?([^\'"\s]+)[\'"]?', content_disposition
            ).group(1)
            path = os.path.join(os.path.dirname(path), filename)

        with open(path, "wb") as f:
            f.write(response.data)

        return path

    def __deserialize_primitive(self, data, klass, model_finder):
        """Deserializes string to primitive type.

        :param data: str.
        :param klass: class literal.
        :param model_finder: ModelFinder instance to find class for
            response_type class literal

        :return: int, long, float, str, bool.
        """
        # TODO obsolete, remove
        try:
            return klass(data)
        except UnicodeEncodeError:
            return str(data)
        except TypeError:
            return data

    def __deserialize_object(self, value):
        """Return an original value.

        :return: object.
        """
        # TODO obsolete, remove
        return value

    def __deserialize_date(self, string):
        """Deserializes string to date.

        :param string: str.
        :return: date.
        """
        # TODO obsolete, remove
        try:
            from dateutil.parser import parse

            return parse(string).date()
        except ImportError:
            return string
        except ValueError:
            raise rest.ApiException(
                status=0, reason="Failed to parse `{0}` as date object".format(string)
            )

    def __deserialize_datatime(self, string):
        """Deserializes string to datetime.

        The string should be in iso8601 datetime format.

        :param string: str.
        :return: datetime.
        """
        # TODO obsolete, remove
        try:
            from dateutil.parser import parse

            return parse(string)
        except ImportError:
            return string
        except ValueError:
            raise rest.ApiException(
                status=0,
                reason=("Failed to parse `{0}` as datetime object".format(string)),
            )

    def __deserialize_model(self, data, klass, model_finder):
        """Deserializes list or dict to model.

        :param data: dict, list.
        :param klass: class literal.
        :param model_finder: ModelFinder instance to find class for
            response_type class literal

        :return: model object.
        """
        # TODO obsolete, remove
        if not klass.openapi_types and not hasattr(klass, "get_real_child_model"):
            return data

        kwargs = {}
        if klass.openapi_types is not None:
            for attr, attr_type in klass.openapi_types.items():
                if (
                    data is not None
                    and klass.attribute_map[attr] in data
                    and isinstance(data, (list, dict))
                ):
                    value = data[klass.attribute_map[attr]]
                    kwargs[attr] = self.__deserialize(value, attr_type, model_finder)

        instance = klass(**kwargs)

        if hasattr(instance, "get_real_child_model"):
            klass_name = instance.get_real_child_model(data)
            if klass_name:
                instance = self.__deserialize(data, klass_name, model_finder)
        return instance

    def get_oauth2_token(self):
        """
        Get oauth2 token dictionary
        :return: dict
        """
        if not self._oauth2_token_getter:
            raise OAuth2TokenGetterError(
                "Invalid oauth2_token_getter={!r} function".format(
                    self._oauth2_token_getter
                )
            )
        return self._oauth2_token_getter()

    def set_oauth2_token(self, token):
        """
        Set oauth2 token
        :param dict token: standard token dictionary
        """
        if not self._oauth2_token_saver:
            raise OAuth2TokenSaverError(
                "Invalid oauth2_token_saver={!r} function".format(
                    self._oauth2_token_saver
                )
            )
        self._oauth2_token_saver(token)

    def refresh_oauth2_token(self):
        """
        Force refresh oauth2 token
        :return: new oauth2 token
        """
        oauth2_token = self.configuration.oauth2_token
        oauth2_token.update_token(**self.get_oauth2_token())
        if oauth2_token.refresh_access_token(self):
            return self.get_oauth2_token()

    def revoke_oauth2_token(self):
        """
        Force revoke oauth2 token
        :return: empty oauth2 token
        """
        oauth2_token = self.configuration.oauth2_token
        oauth2_token.update_token(**self.get_oauth2_token())
        if oauth2_token.revoke_access_token(self):
            return self.get_oauth2_token()

    def get_client_credentials_token(self, app_store_billing=False):
        """
        Obtain oauth2 token using client credentials grant type
        :return: oauth2 token
        """
        oauth2_token = self.configuration.oauth2_token
        if oauth2_token.get_client_credentials_access_token(self, app_store_billing):
            return self.get_oauth2_token()

    def oauth2_token_getter(self, token_getter):
        """
        A decorator to register a callback function for getting oauth2 token

        It is necessary for token synchronisation across the application code.

        :param token_getter: the callback function returning oauth2 token dictionary.
        :return: token_getter to allow this method be used as decorator
        """
        self._oauth2_token_getter = token_getter
        return token_getter

    def oauth2_token_saver(self, token_saver):
        """
        A decorator to register a callback function for saving refreshed
        token while the old token has expired

        It is necessary for using the automatic refresh mechanism.

        :param token_saver: the callback function accepting `token` argument.
        :return: token_saver to allow this method be used as decorator
        """
        self._oauth2_token_saver = token_saver
        return token_saver
