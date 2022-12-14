from .utils import NamespacedClient, query_params, _make_path

class NodesClient(NamespacedClient):
    @query_params('flat_settings', 'human', 'timeout')
    def info(self, node_id=None, metric=None, params=None):
        """
        The cluster nodes info API allows to retrieve one or more (or all) of
        the cluster nodes information.
        `<http://www.elastic.co/guide/en/elasticsearchone/reference/current/cluster-nodes-info.html>`_

        :arg node_id: A comma-separated list of node IDs or names to limit the
            returned information; use `_local` to return information from the
            node you're connecting to, leave empty to get information from all
            nodes
        :arg metric: A comma-separated list of metrics you wish returned. Leave
            empty to return all.
        :arg flat_settings: Return settings in flat format (default: false)
        :arg human: Whether to return time and byte values in human-readable
            format., default False
        :arg timeout: Explicit operation timeout
        """
        _, data = self.transport.perform_request('GET', _make_path('_nodes',
            node_id, metric), params=params)
        return data

    @query_params('delay', 'exit')
    def shutdown(self, node_id=None, params=None):
        """
        The nodes shutdown API allows to shutdown one or more (or all) nodes in
        the cluster.
        `<http://www.elastic.co/guide/en/elasticsearchone/reference/current/cluster-nodes-shutdown.html>`_

        :arg node_id: A comma-separated list of node IDs or names to perform the
            operation on; use `_local` to perform the operation on the node
            you're connected to, leave empty to perform the operation on all
            nodes
        :arg delay: Set the delay for the operation (default: 1s)
        :arg exit: Exit the JVM as well (default: true)
        """
        _, data = self.transport.perform_request('POST', _make_path('_cluster',
            'nodes', node_id, '_shutdown'), params=params)
        return data

    @query_params('completion_fields', 'fielddata_fields', 'fields', 'groups',
        'human', 'level', 'types')
    def stats(self, node_id=None, metric=None, index_metric=None, params=None):
        """
        The cluster nodes stats API allows to retrieve one or more (or all) of
        the cluster nodes statistics.
        `<http://www.elastic.co/guide/en/elasticsearchone/reference/current/cluster-nodes-stats.html>`_

        :arg node_id: A comma-separated list of node IDs or names to limit the
            returned information; use `_local` to return information from the
            node you're connecting to, leave empty to get information from all
            nodes
        :arg metric: Limit the information returned to the specified metrics
        :arg index_metric: Limit the information returned for `indices` metric
            to the specific index metrics. Isn't used if `indices` (or `all`)
            metric isn't specified.
        :arg completion_fields: A comma-separated list of fields for `fielddata`
            and `suggest` index metric (supports wildcards)
        :arg fielddata_fields: A comma-separated list of fields for `fielddata`
            index metric (supports wildcards)
        :arg fields: A comma-separated list of fields for `fielddata` and
            `completion` index metric (supports wildcards)
        :arg groups: A comma-separated list of search groups for `search` index
            metric
        :arg human: Whether to return time and byte values in human-readable
            format., default False
        :arg level: Return indices stats aggregated at node, index or shard
            level, default 'node', valid choices are: 'node', 'indices',
            'shards'
        :arg timeout: Explicit operation timeout
        :arg types: A comma-separated list of document types for the `indexing`
            index metric
        """
        _, data = self.transport.perform_request('GET', _make_path('_nodes',
            node_id, 'stats', metric, index_metric), params=params)
        return data

    @query_params('doc_type', 'ignore_idle_threads', 'interval', 'snapshots',
        'threads', 'timeout')
    def hot_threads(self, node_id=None, params=None):
        """
        An API allowing to get the current hot threads on each node in the cluster.
        `<http://www.elastic.co/guide/en/elasticsearchone/reference/current/cluster-nodes-hot-threads.html>`_

        :arg node_id: A comma-separated list of node IDs or names to limit the
            returned information; use `_local` to return information from the
            node you're connecting to, leave empty to get information from all
            nodes
        :arg doc_type: The type to sample (default: cpu), valid choices are:
            'cpu', 'wait', 'block'
        :arg ignore_idle_threads: Don't show threads that are in known-idle
            places, such as waiting on a socket select or pulling from an empty
            task queue (default: true)
        :arg interval: The interval for the second sampling of threads
        :arg snapshots: Number of samples of thread stacktrace (default: 10)
        :arg threads: Specify the number of threads to provide information for
            (default: 3)
        :arg timeout: Explicit operation timeout
        """
        # avoid python reserved words
        if params and 'type_' in params:
            params['type'] = params.pop('type_')
        _, data = self.transport.perform_request('GET', _make_path('_cluster',
            'nodes', node_id, 'hotthreads'), params=params)
        return data
