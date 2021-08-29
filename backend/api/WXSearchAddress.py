# -*- coding: utf-8 -*-
from utils.MemberService import MemberService
from flask import Blueprint, request, jsonify
import DataBaseFolder.Interface.UserBaseModify as U

route_WXSearchAddress = Blueprint('WXSearchAddress', __name__)