.. ...........................................................................
.. Copyright (c) IBM Corporation 2020                                        .
.. ...........................................................................

Operate z/OS Jobs
=================

**IBM z/OSMF collection** provides capabilities to work with batch jobs on a z/OS system using Ansible playbooks. There are three roles provided to interact with z/OS jobs REST services. These roles drive z/OS jobs RESTful services to operate batch jobs.

Roles
-----

* `zmf_job_complete`_:

  This role can be used to submit a job to run on z/OS, check its return code after the job is completed, and check the user specified content from spool files, and save the user specified spool files locally on control node.

* `zmf_job_query`_:

  This role can be used to query a job running on z/OS, check its return code, and check the user specified content from spool files, and save the user specified spool files locally on control node.

Requirements
------------

See the section `Requirements`_.

Sample Playbooks
----------------

See the section `Playbooks`_.


.. _zmf_job_complete:
   roles/README_zmf_job_complete.html
.. _zmf_job_query:
   roles/README_zmf_job_query.html
.. _Requirements:
   requirements_job.html
.. _Playbooks:
   playbooks.html